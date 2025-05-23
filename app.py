from transformers import pipeline
import gradio as gr


model = pipeline(
    "summarization",
)

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary


# create an interface for the model
with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter the text to summurize ",lines=4)
    gr.Interface(fn=predict, inputs="textbox", outputs="text")
demo.launch()