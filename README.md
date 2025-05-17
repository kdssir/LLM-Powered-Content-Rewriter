
# LLM Powered Content Rewriter App

A simple web app to rewrite emails or resumes in different tones using a local or cloud-based Large Language Model (LLM). Built with **FastAPI** backend, **Streamlit** frontend, and integrated with LLMs like **Mistral** or **LLaMA 3** via Ollama or other providers.

---

## Features

- Rewrite email or resume text in tones like formal, friendly, persuasive, etc.
- Easy-to-use Streamlit UI for input and output display.
- FastAPI backend for handling requests and interacting with the LLM.
- Modular code to swap LLM providers (Ollama, Groq, Together.ai, etc.).
- Simple prompt templating for flexible rewriting instructions.

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running with the chosen LLM model (e.g. `mistral` or `llama3`)
- Alternatively, an API key for cloud LLM providers (Groq, Together.ai, etc.)

---

### Installation

```

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Running the Application

1. Start the LLM server (if using Ollama):

```bash
ollama run mistral
# or
ollama run llama3
```

2. Start the FastAPI backend:

```bash
uvicorn backend.main:app --reload --port 8000
```

3. Start the Streamlit frontend:

```bash
streamlit run frontend/app.py
```

4. Open your browser at `http://localhost:8501` to use the UI.

---

## Usage

- Enter the text you want to rewrite.
- Select document type: email or resume.
- Choose the desired tone.
- Click **Rewrite** to get the rewritten text.

---

## Project Structure

```
email_rewriter_app/
├── backend/
│   ├── main.py          # FastAPI app
│   ├── llm.py           # LLM integration and prompt logic
│   ├── models.py        # Request validation schema
├── frontend/
│   └── app.py           # Streamlit UI
├── requirements.txt     # Python dependencies
├── README.md            # This file
```

---

## Customization

- Change or extend tones in `frontend/app.py`.
- Swap or upgrade LLM by modifying `backend/llm.py`.
- Enhance prompt templates for more nuanced rewriting.

---

## Troubleshooting

- Ensure Ollama is running and the model is loaded.
- Check FastAPI logs for backend errors.
- Verify correct API keys and environment variables if using cloud LLMs.
- Make sure ports 8000 (backend) and 8501 (Streamlit) are free.

---

## Credits

- **Ollama** — Local LLM platform  
  [https://ollama.com](https://ollama.com)

- **Mistral** — Open-weight foundation models  
  [https://mistral.ai](https://mistral.ai)

- **FastAPI** — Modern, fast web framework for building APIs with Python 3.7+  
  [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)

- **Streamlit** — The fastest way to build data apps in Python  
  [https://streamlit.io](https://streamlit.io)

- **LangChain** — Framework for building applications with LLMs  
  [https://langchain.com](https://langchain.com)



