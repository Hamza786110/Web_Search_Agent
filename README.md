# Web Search Agent

A real-time AI-powered web search assistant built with **LangChain**, **Groq**, **Tavily**, and **Streamlit**. Ask any question and get live, accurate answers pulled straight from the web — all through a clean chat-style UI.

---

## Demo

Enter a query in the Streamlit interface and the agent searches the web via Tavily and returns a summarized, AI-generated answer powered by Groq's `qwen3-32b` model.

---

## Features

- **Groq LLM** — Uses `qwen/qwen3-32b` via `langchain-groq` for fast, intelligent responses
- **Tavily Search** — Performs advanced web searches and returns concise answers
- **LangChain Agent** — Tool-calling agent that decides when and how to search
- **Streamlit UI** — Simple, interactive browser-based interface
- **Environment-based Config** — API keys managed securely via `.env`

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Agent Framework | LangChain + LangGraph |
| Language Model | Groq (`qwen/qwen3-32b`) |
| Search Tool | Tavily API |
| Frontend | Streamlit |
| Language | Python 3.8+ |

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/Hamza786110/Web_Search_Agent.git
cd Web_Search_Agent

# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root with your API keys:

```env
GROQ_API_KEY="your-groq-api-key"
TAVILY_API_KEY="your-tavily-api-key"
```

> - Get a Groq API key at [console.groq.com](https://console.groq.com)
> - Get a Tavily API key at [tavily.com](https://tavily.com)

---

## Running the App

```bash
streamlit run web_Search_agent.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Project Structure

```
Web_Search_Agent/
├── web_Search_agent.py   # Main app — Streamlit UI + LangChain agent
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not committed)
└── .gitignore            # Ignores venv, cache, build files
```

---

## Contributing

Contributions are welcome! Fork the repo and open a pull request with your improvements.

---
