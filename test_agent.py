from agent_workflow import run_agent

query_search = "Find me a flight from New York to Paris on 2025-06-07 under $500."
response_search = run_agent(query_search)
print("Search Response:\n", response_search)

query_book = '{"intent": "book_flight", "flight_id": "NYC123"}'
response_book = run_agent(query_book)
print("\nBooking Response:\n", response_book)
