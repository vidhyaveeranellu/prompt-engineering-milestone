
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from gemini_client import generate_response, save_result


problem = """
A shopkeeper buys 5 notebooks for ₹40 each.
He sells each notebook for ₹55 each.
He spends ₹25 on transportation.

Calculate his total profit.
"""


# Direct prompt
direct_prompt = f"""
Solve this problem and give only the final profit.

{problem}
"""


# Step-by-step prompt
step_prompt = f"""
Solve the following mathematical problem.

Show the necessary calculation steps clearly:
1. Calculate total purchase cost.
2. Calculate total selling price.
3. Include transportation cost.
4. Calculate final profit.

Do not skip any calculation.

Problem:
{problem}
"""


print("Running direct prompt...")
direct_output = generate_response(direct_prompt)

print("\nRunning step-by-step prompt...")
step_output = generate_response(step_prompt)


# Independently calculated expected answer
expected_profit = 50

print("\n========== DIRECT OUTPUT ==========")
print(direct_output)

print("\n========== STEP-BY-STEP OUTPUT ==========")
print(step_output)

print("\nExpected profit: ₹", expected_profit)


report = f"""
# Experiment 2: Direct vs Step-by-Step Prompting

## Problem

{problem}

## Direct prompt

{direct_prompt}

## Actual direct output

{direct_output}

## Step-by-step prompt

{step_prompt}

## Actual step-by-step output

{step_output}

## Independently calculated answer

Purchase cost = 5 × 40 = ₹200

Selling price = 5 × 55 = ₹275

Total cost = 200 + 25 = ₹225

Profit = 275 - 225 = ₹50

Expected profit = ₹50

## Analysis

Compare whether both responses contain the correct final answer.
Check whether the step-by-step prompt makes the calculations
easier to verify. Record any errors honestly.
"""

save_result("02_reasoning.md", report)
