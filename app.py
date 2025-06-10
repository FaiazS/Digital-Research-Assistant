from dotenv import load_dotenv

import gradio as gr

from research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):

    async for chunk in ResearchManager().run(query):

        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as user_interface:

    gr.Markdown("Digital Research Assistant")

    query = gr.Textbox(label="Hi there, what would you like to research on today?")

    execute_button = gr.Button("Execute", variant="primary")

    research_report = gr.Markdown(label="Research Report")

    execute_button.click(fn= run, inputs=query, outputs=research_report)

    query.submit(fn = run, inputs = query, outputs = research_report)


user_interface.launch()