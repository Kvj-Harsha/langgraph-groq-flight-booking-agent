import gradio as gr
from agent_workflow import run_agent

def respond(user_msg, history, context_dict):
    history = history or []
    context_dict = context_dict or {}

    # Append user message
    history.append({"role": "user", "content": user_msg})

    # Run agent with context
    reply = run_agent(user_msg, context_dict)

    # Append assistant reply
    history.append({"role": "assistant", "content": reply})

    return history, history, context_dict


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # ✈️ Flight Booking Assistant
    You can ask me to:
    - **Find flights** — “Find me a flight from NYC to Paris under $500”
    - **Book flights** — “Okay, book that flight”
    
    ℹ️ This is a mock flight assistant. Data is fictional but behaves realistically!
    """)

    chatbot = gr.Chatbot(label="Flight Chat", type="messages")
    msg = gr.Textbox(placeholder="e.g., Book me a flight to London...", label="Your Message")
    
    state = gr.State([])          # chat history
    context = gr.State({})        # booking context (like last_flight_id)

    msg.submit(respond, [msg, state, context], [chatbot, state, context])

demo.launch()