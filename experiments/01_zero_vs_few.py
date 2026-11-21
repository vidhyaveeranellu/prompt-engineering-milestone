
import sys
from pathlib import Path

# Allow importing gemini_client from the root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from gemini_client import generate_response, save_result


# Test dataset with expected labels
reviews = [
    {
        "review": "This product is amazing. I really love it!",
        "expected": "Positive"
    },
    {
        "review": "The product stopped working after one day.",
        "expected": "Negative"
    },
    {
        "review": "The package arrived yesterday.",
        "expected": "Neutral"
    },
    {
        "review": "Excellent quality and very fast delivery.",
        "expected": "Positive"
    },
    {
        "review": "Very poor quality. I regret buying it.",
        "expected": "Negative"
    }
]


# Zero-shot prompt
def zero_shot_prompt(review):
    return f"""
Classify the sentiment of this customer review.

Choose only one label:
Positive, Negative, or Neutral.

Return only the label.

Review: {review}
"""


# Few-shot prompt with four examples
def few_shot_prompt(review):
    return f"""
You are a customer review sentiment classifier.

Classify each review as Positive, Negative, or Neutral.

Here are some examples:

Review: I absolutely love this product.
Sentiment: Positive

Review: The product is damaged and useless.
Sentiment: Negative

Review: The order arrived on Monday.
Sentiment: Neutral

Review: Fantastic quality and excellent service.
Sentiment: Positive

Now classify this review.

Review: {review}

Return only one label:
Positive, Negative, or Neutral.

Sentiment:
"""


def clean_label(output):
    label = output.strip().split()[0].strip(".,:!").lower()

    if label in ["positive", "negative", "neutral"]:
        return label.capitalize()

    return "Invalid"


zero_correct = 0
few_correct = 0

report = "# Experiment 1: Zero-shot vs Few-shot\n\n"

for index, item in enumerate(reviews, start=1):

    review = item["review"]
    expected = item["expected"]

    print(f"\nTEST {index}")
    print("Review:", review)

    # Zero-shot execution
    zero_prompt = zero_shot_prompt(review)
    zero_output = generate_response(zero_prompt)

    # Few-shot execution
    few_prompt = few_shot_prompt(review)
    few_output = generate_response(few_prompt)

    zero_label = clean_label(zero_output)
    few_label = clean_label(few_output)

    zero_result = zero_label == expected
    few_result = few_label == expected

    zero_correct += int(zero_result)
    few_correct += int(few_result)

    # Print actual outputs
    print("\nZero-shot output:", zero_output)
    print("Few-shot output:", few_output)
    print("Expected:", expected)

    report += f"""
## Test {index}

Review: {review}

Expected label: {expected}

### Zero-shot prompt

{zero_prompt}

### Actual zero-shot output

{zero_output}

Correct: {zero_result}

### Few-shot prompt

{few_prompt}

### Actual few-shot output

{few_output}

Correct: {few_result}

---
"""

zero_accuracy = zero_correct / len(reviews) * 100
few_accuracy = few_correct / len(reviews) * 100

summary = f"""
## Results

Total test reviews: {len(reviews)}

Zero-shot correct: {zero_correct}/{len(reviews)}
Zero-shot accuracy: {zero_accuracy:.2f}%

Few-shot correct: {few_correct}/{len(reviews)}
Few-shot accuracy: {few_accuracy:.2f}%

"""

report += summary

save_result("01_zero_vs_few.md", report)

print("\n========== FINAL COMPARISON ==========")
print(summary)
