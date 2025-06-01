# Flight Booking Agent

This repository contains a flight booking AI assistant powered by a Groq LLM backend and integrated with a simple agent workflow. It supports searching flights, filtering by price, formatting results, and booking flights.

---

## Project Structure

- **Local Testing Files**: For local development and debugging.
- **Hugging Face Space Files**: For deploying the agent on Hugging Face Spaces with a web UI.

---

# Workflow

<img src="https://github.com/user-attachments/assets/561d72cb-e217-4cf2-a285-964ef3f026f8" />

---

## Local Testing

These files help you test the components and the agent workflow locally on your machine.

- `test_llm.py` — Simple script to test the LLM API call.
- `test_agent.py` — Script to test the agent workflow end-to-end in CLI.
- `llm/groq_client.py` — Module to call the Groq API.
- `agents/steps.py` — Core agent functions: search flights, filter, format, book.
- `agent_workflow.py` — Main agent logic parsing user input and orchestrating steps.

### Running Locally

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flight-booking-agent.git
    cd flight-booking-agent
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate   # Windows PowerShell
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set your Groq API key environment variable:

    ```bash
    export GROQ_API_KEY="your_api_key_here"    # Linux/macOS
    setx GROQ_API_KEY "your_api_key_here"       # Windows (restart shell after)
    ```

5. Run the test scripts:

    ```bash
    python test_llm.py
    python test_agent.py
    ```

---

## Hugging Face Space Deployment

These files power the web UI and full agent experience on Hugging Face Spaces.

- `app.py` — Gradio app frontend and backend integration.
- `agents/steps.py` — Same core agent functions as local.
- `agent_workflow.py` — Same agent orchestration logic.
- `data/flights.json` — Sample flight data used for booking simulation.
- `requirements.txt` — Python dependencies for Hugging Face environment.

## LLM Configuration

The project uses the Groq LLM API with the default model set to `"llama3-8b-8192"`.

The `call_llm` function signature is:

```python
def call_llm(messages, model="llama3-8b-8192", temperature=0.7):
```

### Running on Hugging Face Spaces

1. Push the repository to a new Hugging Face Space repository.

2. Add the secret environment variable `GROQ_API_KEY` via the Space settings page.

3. The Space will automatically install dependencies and launch the app.

4. Open the Space URL to interact with the flight booking assistant.

---

## How It Works

- User inputs a request (e.g., "Find me a flight from NYC to Paris next Friday under $500").
- The agent uses the LLM to parse intent and entities.
- It searches available flights from local JSON data.
- Filters flights by max price.
- Displays flight options to the user.
- The user can then book a flight by saying, for example, "Ok, book that flight".
- The booking is simulated and confirmed in the UI.

---

## Future Improvements

- Store chat history between user and agent.
- Improve UI theme and interaction.
- Connect to real flight booking APIs.
- Add natural language booking commands beyond exact flight IDs.

---

## License

MIT License — see LICENSE file for details.

---

If you want help setting up or customizing anything, just ask!
