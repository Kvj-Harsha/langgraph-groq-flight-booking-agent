import json
from datetime import datetime

# Load mock flight data once
with open("data/flights.json", "r") as f:
    FLIGHTS = json.load(f)

def search_flights(origin, destination, date_str):
    """
    Search flights by origin, destination, and date (YYYY-MM-DD string).
    Returns a list of matching flight dicts.
    """
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    results = [
        flight for flight in FLIGHTS
        if flight["from"].lower() == origin.lower()
        and flight["to"].lower() == destination.lower()
        and datetime.strptime(flight["date"], "%Y-%m-%d").date() == date
    ]
    return results

def filter_flights(flights, max_price=None):
    """
    Filter flights by maximum price if provided.
    """
    if max_price is None:
        return flights
    return [f for f in flights if f["price"] <= max_price]

def confirm_booking(flight_id):
    """
    Mock booking confirmation.
    Returns a confirmation message.
    """
    flight = next((f for f in FLIGHTS if f["flight_id"] == flight_id), None)
    if not flight:
        return "Sorry, I couldn't find that flight to book."
    return f"Your flight {flight_id} from {flight['from']} to {flight['to']} on {flight['date']} has been booked successfully!"

def format_flights(flights):
    """
    Format list of flights into human-readable string.
    """
    if not flights:
        return "No flights found matching your criteria."
    lines = []
    for f in flights:
        lines.append(
            f"- {f['airline']} flight {f['flight_id']} from {f['from']} to {f['to']} on {f['date']} at {f['departure_time']}, Price: ${f['price']}"
        )
    return "\n".join(lines)
