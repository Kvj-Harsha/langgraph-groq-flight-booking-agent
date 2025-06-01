import gradio as gr
from agent_workflow import run_agent

def chat_with_agent(user_input):
    response = run_agent(user_input)
    return response

iface = gr.Interface(
    fn=chat_with_agent,
    inputs=gr.Textbox(lines=3, placeholder="Ask me to find or book a flight..."),
    outputs="text",
    title="Flight Booking Agent",
    description="Ask for flights or book them using natural language."
)

if __name__ == "__main__":
    iface.launch()
