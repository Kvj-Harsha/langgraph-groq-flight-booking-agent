import requests

# Direct assignment for local testing
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

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

    response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
