# agent_workflow_simple.py

from llm.groq_client import call_llm
from agents.steps import search_flights, filter_flights, format_flights, confirm_booking
import json

def llm_call(messages):
    return call_llm(messages)

def parse_input(user_input):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a flight booking assistant. "
                "Given the user input, ONLY respond with a valid JSON containing these keys if present: "
                "intent, origin, destination, date (YYYY-MM-DD), max_price (number), flight_id. "
                "Do NOT add any extra text or explanations."
            ),
        },
        {"role": "user", "content": user_input},
    ]
    response = llm_call(prompt)
    print("LLM raw response:", response)  # Debug print to see raw LLM output
    try:
        return json.loads(response)
    except Exception as e:
        print("JSON decode error:", e)
        return {}

def run_agent(user_input, context=None):
    context = context or {}
    last_flight_id = context.get("last_flight_id")

    parsed = parse_input(user_input)
    print("LLM parsed:", parsed)

    if parsed.get("intent") == "book_flight":
        # fallback to last flight if not explicitly mentioned
        flight_id = parsed.get("flight_id") or last_flight_id
        if not flight_id:
            return "No flight ID provided and no previous flight to book."
        return confirm_booking(flight_id)

    origin = parsed.get("origin")
    destination = parsed.get("destination")
    date = parsed.get("date")
    max_price = parsed.get("max_price")

    if not (origin and destination and date):
        return "Please provide origin, destination, and date."

    flights = search_flights(origin, destination, date)
    filtered = filter_flights(flights, max_price)
    formatted = format_flights(filtered)

    # If a flight was found, save its ID for future use
    if filtered:
        context["last_flight_id"] = filtered[0]["flight_id"]

    return formatted

