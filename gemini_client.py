
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def generate_response(prompt, temperature=0):
    """Send a prompt to Gemini and return its actual response."""

    response = client.interactions.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text


def save_result(filename, content):
    """Save experimental results in the results folder."""

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    file_path = results_dir / filename

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)
        file.write("\n\n" + "=" * 70 + "\n\n")

    print(f"Saved result: {file_path}")
