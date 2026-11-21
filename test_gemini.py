from gemini_client import generate_response, MODEL

print("Testing Gemini API...")
print("Model:", MODEL)

response = generate_response(
    "What is prompt engineering? Explain in two sentences."
)

print("\nGemini Response:")
print(response)
