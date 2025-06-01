# test_llm.py
from llm.groq_client import call_llm
import os

# TEMP: manually set key here for local test (optional)
os.environ["GROQ_API_KEY"] = "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"

if not os.getenv("GROQ_API_KEY"):
    print("❌ Missing GROQ_API_KEY env variable")
    exit()

response = call_llm([
    {"role": "system", "content": "You are a helpful flight booking assistant."},
    {"role": "user", "content": "Find me a flight from New York to Paris next Friday under $500."}
])

print("🧠 Response from LLM:")
print(response)
