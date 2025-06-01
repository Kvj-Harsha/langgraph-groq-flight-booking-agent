from agents.steps import search_flights, filter_flights, format_flights, confirm_booking

flights = search_flights("New York", "Paris", "2025-06-07")
filtered = filter_flights(flights, max_price=500)
print(format_flights(filtered))

confirmation = confirm_booking("NYC123")
print(confirmation)
