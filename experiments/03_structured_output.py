
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from gemini_client import client, MODEL, save_result


# Define the JSON schema
ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "customer_name": {
            "type": "string"
        },
        "product": {
            "type": "string"
        },
        "date": {
            "type": "string"
        },
        "amount": {
            "type": "number"
        }
    },
    "required": [
        "customer_name",
        "product",
        "date",
        "amount"
    ]
}


# Five test inputs with known expected values
test_inputs = [
    {
        "input": "Ravi ordered a laptop on 2026-11-20 for Rs. 55000.",
        "expected": {
            "customer_name": "Ravi",
            "product": "laptop",
            "date": "2026-11-20",
            "amount": 55000
        }
    },
    {
        "input": "On 2026-11-18, Priya purchased a mobile phone worth Rs. 18500.",
        "expected": {
            "customer_name": "Priya",
            "product": "mobile phone",
            "date": "2026-11-18",
            "amount": 18500
        }
    },
    {
        "input": "Arun bought a keyboard for Rs. 1500 on 2026-11-15.",
        "expected": {
            "customer_name": "Arun",
            "product": "keyboard",
            "date": "2026-11-15",
            "amount": 1500
        }
    },
    {
        "input": "Meena purchased headphones on 2026-11-14. The price was 2000 rupees.",
        "expected": {
            "customer_name": "Meena",
            "product": "headphones",
            "date": "2026-11-14",
            "amount": 2000
        }
    },
    {
        "input": "Karthik placed an order for a monitor costing Rs. 12000 on 2026-11-12.",
        "expected": {
            "customer_name": "Karthik",
            "product": "monitor",
            "date": "2026-11-12",
            "amount": 12000
        }
    }
]


def extract_order(text):

    prompt = f"""
You are an accurate information extraction assistant.

Extract the customer order details from the given text.

Return exactly these four fields:
- customer_name
- product
- date
- amount

Rules:
1. Do not invent missing information.
2. Preserve the customer's name.
3. Extract the product name.
4. Format the date as YYYY-MM-DD.
5. Amount must be a numeric value without currency symbols.
6. Do not add any extra fields.

Customer order:
{text}
"""

    response = client.interactions.create(
        model=MODEL,
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ORDER_SCHEMA
        }
    )

    return prompt, response.output_text


def validate_output(raw_output, expected):

    try:
        data = json.loads(raw_output)

        required_keys = [
            "customer_name",
            "product",
            "date",
            "amount"
        ]

        # Check required fields
        if set(data.keys()) != set(required_keys):
            return False, data, "Incorrect JSON keys"

        # Check data types
        if not isinstance(data["customer_name"], str):
            return False, data, "Invalid customer_name type"

        if not isinstance(data["product"], str):
            return False, data, "Invalid product type"

        if not isinstance(data["date"], str):
            return False, data, "Invalid date type"

        if not isinstance(data["amount"], (int, float)):
            return False, data, "Invalid amount type"

        # Check extracted values
        if data != expected:
            return False, data, "Extracted values do not match expected values"

        return True, data, "Valid and correct"

    except (json.JSONDecodeError, TypeError):
        return False, None, "Invalid JSON"


success_count = 0

report = "# Experiment 3: Structured JSON Output\n\n"

for index, item in enumerate(test_inputs, start=1):

    print(f"\n========== TEST {index} ==========")

    input_text = item["input"]
    expected = item["expected"]

    print("Input:", input_text)

    prompt, raw_output = extract_order(input_text)

    print("\nActual Gemini output:")
    print(raw_output)

    success, data, message = validate_output(
        raw_output,
        expected
    )

    if success:
        success_count += 1

    print("\nValidation:", message)

    report += f"""
## Test {index}

### Input

{input_text}

### Actual prompt

{prompt}

### Actual raw Gemini output

```json
{raw_output}
```

### Expected output

```json
{json.dumps(expected, indent=4)}
```

### Validation result

{message}

Success: {success}

---
"""


success_rate = success_count / len(test_inputs) * 100

summary = f"""
## Overall Results

Total test inputs: {len(test_inputs)}

Successful outputs: {success_count}

Failed outputs: {len(test_inputs) - success_count}

Success rate: {success_rate:.2f}%
"""

report += summary

save_result("03_structured_output.md", report)

print("\n========== FINAL RESULTS ==========")
print(summary)
