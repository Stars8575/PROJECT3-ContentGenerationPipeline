import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please create a .env file."
    )

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Model Configuration
MODEL_NAME = "gemini-2.0-flash-lite"

# Generation Configuration
GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.9,
    "max_output_tokens": 2048,
}