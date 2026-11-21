# Experiment 3: Structured JSON Output


## Test 1

### Input

Ravi ordered a laptop on 2026-11-20 for Rs. 55000.

### Actual prompt


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
Ravi ordered a laptop on 2026-11-20 for Rs. 55000.


### Actual raw Gemini output

```json
{"customer_name":"Ravi","product":"laptop","date":"2026-11-20","amount":55000}
```

### Expected output

```json
{
    "customer_name": "Ravi",
    "product": "laptop",
    "date": "2026-11-20",
    "amount": 55000
}
```

### Validation result

Valid and correct

Success: True

---

## Test 2

### Input

On 2026-11-18, Priya purchased a mobile phone worth Rs. 18500.

### Actual prompt


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
On 2026-11-18, Priya purchased a mobile phone worth Rs. 18500.


### Actual raw Gemini output

```json
{"customer_name":"Priya","product":"mobile phone","date":"2026-11-18","amount":18500}
```

### Expected output

```json
{
    "customer_name": "Priya",
    "product": "mobile phone",
    "date": "2026-11-18",
    "amount": 18500
}
```

### Validation result

Valid and correct

Success: True

---

## Test 3

### Input

Arun bought a keyboard for Rs. 1500 on 2026-11-15.

### Actual prompt


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
Arun bought a keyboard for Rs. 1500 on 2026-11-15.


### Actual raw Gemini output

```json
{"customer_name":"Arun","product":"keyboard","date":"2026-11-15","amount":1500}
```

### Expected output

```json
{
    "customer_name": "Arun",
    "product": "keyboard",
    "date": "2026-11-15",
    "amount": 1500
}
```

### Validation result

Valid and correct

Success: True

---

## Test 4

### Input

Meena purchased headphones on 2026-11-14. The price was 2000 rupees.

### Actual prompt


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
Meena purchased headphones on 2026-11-14. The price was 2000 rupees.


### Actual raw Gemini output

```json
{"customer_name":"Meena","product":"headphones","date":"2026-11-14","amount":2000}
```

### Expected output

```json
{
    "customer_name": "Meena",
    "product": "headphones",
    "date": "2026-11-14",
    "amount": 2000
}
```

### Validation result

Valid and correct

Success: True

---

## Test 5

### Input

Karthik placed an order for a monitor costing Rs. 12000 on 2026-11-12.

### Actual prompt


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
Karthik placed an order for a monitor costing Rs. 12000 on 2026-11-12.


### Actual raw Gemini output

```json
{"customer_name":"Karthik","product":"monitor","date":"2026-11-12","amount":12000}
```

### Expected output

```json
{
    "customer_name": "Karthik",
    "product": "monitor",
    "date": "2026-11-12",
    "amount": 12000
}
```

### Validation result

Valid and correct

Success: True

---

## Overall Results

Total test inputs: 5

Successful outputs: 5

Failed outputs: 0

Success rate: 100.00%


======================================================================

