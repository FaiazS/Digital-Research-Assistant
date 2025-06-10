# 🧠Digital-Research-Assistant
---
An end-to-end autonomous research system that takes a user query and delivers a full-length research report—summarized, well-structured, and emailed to your inbox using SendGrid.

✨ Powered by OpenAI GPT-4o Agents + Web Search + Email Delivery + Gradio UI  

⚡ Application link: https://huggingface.co/spaces/FaiazAI/Digital_Research_Assistant

---

## 📌 Features

- 🔍 **AI-powered Web Search Planning** — Breaks down a query into targeted search terms.
  
- 🌐 **Live Web Search** — Uses tools to retrieve the latest info from the internet.
  
- 📝 **Cohesive Report Generation** — Generates high-quality, coherent research content.
  
- 📧 **Email Delivery** — Sends HTML-formatted report via SendGrid.
  
- 🖥️ **Gradio UI** — Simple browser-based interface to run your research.
  
---

## 🧱 System Architecture

```mermaid
flowchart TD
    A[User submits research query] --> B[Research Planner Agent]
    B --> C[Search Plan - 3 search items]
    C --> D[Web Search Agent - Called 3 times]
    D --> E[Search Summaries]
    E --> F[Research Writer Agent]
    F --> G[Markdown Report]
    G --> H[Email Agent]
    H --> I[Email Sent!]
    G --> J[Display in Gradio UI]

```
## 🗂 Folder Structure

```
.
├── app.py                     # Gradio interface entry point
├── research_manager.py       # Main controller for research execution
├── agents/
│   ├── research_writer.py
│   ├── web_searcher.py
│   ├── research_planner.py
│   ├── email_agent.py
├── requirements.txt
├── .env                      # Local secrets file (replaced with HF secrets for Hugging Face)
└── README.md
```
---

## 💡 Sample Prompt

> _"AI's contribution in tackling and mitigating the impacts of Climate Change."_

---

## 🧠 Built With

- GPT-4o Agents (`openai-agents`)
  
- SendGrid Email API
  
- Python `asyncio` + modularization
  
- Gradio UI for interactivity
  
- Hugging Face Spaces for deployment

---

## 📬 Author

**Faiaz Ahmed**  
[LinkedIn](https://www.linkedin.com/in/faiazahmed22/) • [Email](mailto:faiazrex8@gmail.com)
