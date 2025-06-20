import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY not set in environment variables.")

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def call_llm(messages, model="llama3-8b-8192", temperature=0.7):
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        response_json = response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"LLM request failed: {e}")
    except ValueError:
        raise RuntimeError("Failed to parse JSON response from Groq API")

    if "choices" not in response_json or not response_json["choices"]:
        raise ValueError("Unexpected response format from Groq API")

    return response_json["choices"][0]["message"]["content"]
