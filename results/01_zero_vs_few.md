# Experiment 1: Zero-shot vs Few-shot


## Test 1

Review: This product is amazing. I really love it!

Expected label: Positive

### Zero-shot prompt


Classify the sentiment of this customer review.

Choose only one label:
Positive, Negative, or Neutral.

Return only the label.

Review: This product is amazing. I really love it!


### Actual zero-shot output

Positive

Correct: True

### Few-shot prompt


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

Review: This product is amazing. I really love it!

Return only one label:
Positive, Negative, or Neutral.

Sentiment:


### Actual few-shot output

Positive

Correct: True

---

## Test 2

Review: The product stopped working after one day.

Expected label: Negative

### Zero-shot prompt


Classify the sentiment of this customer review.

Choose only one label:
Positive, Negative, or Neutral.

Return only the label.

Review: The product stopped working after one day.


### Actual zero-shot output

Negative

Correct: True

### Few-shot prompt


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

Review: The product stopped working after one day.

Return only one label:
Positive, Negative, or Neutral.

Sentiment:


### Actual few-shot output

Negative

Correct: True

---

## Test 3

Review: The package arrived yesterday.

Expected label: Neutral

### Zero-shot prompt


Classify the sentiment of this customer review.

Choose only one label:
Positive, Negative, or Neutral.

Return only the label.

Review: The package arrived yesterday.


### Actual zero-shot output

Neutral

Correct: True

### Few-shot prompt


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

Review: The package arrived yesterday.

Return only one label:
Positive, Negative, or Neutral.

Sentiment:


### Actual few-shot output

Neutral

Correct: True

---

## Test 4

Review: Excellent quality and very fast delivery.

Expected label: Positive

### Zero-shot prompt


Classify the sentiment of this customer review.

Choose only one label:
Positive, Negative, or Neutral.

Return only the label.

Review: Excellent quality and very fast delivery.


### Actual zero-shot output

Positive

Correct: True

### Few-shot prompt


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

Review: Excellent quality and very fast delivery.

Return only one label:
Positive, Negative, or Neutral.

Sentiment:


### Actual few-shot output

Positive

Correct: True

---

## Test 5

Review: Very poor quality. I regret buying it.

Expected label: Negative

### Zero-shot prompt


Classify the sentiment of this customer review.

Choose only one label:
Positive, Negative, or Neutral.

Return only the label.

Review: Very poor quality. I regret buying it.


### Actual zero-shot output

Negative

Correct: True

### Few-shot prompt


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

Review: Very poor quality. I regret buying it.

Return only one label:
Positive, Negative, or Neutral.

Sentiment:


### Actual few-shot output

Negative

Correct: True

---

## Results

Total test reviews: 5

Zero-shot correct: 5/5
Zero-shot accuracy: 100.00%

Few-shot correct: 5/5
Few-shot accuracy: 100.00%



======================================================================

