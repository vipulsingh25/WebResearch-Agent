# Web Research Agent

A powerful web research assistant that accepts research queries, searches the web, extracts and analyzes content, and delivers concise research summaries — powered by Gemini and Streamlit.

---

## 🚀 Features
- Query Analysis & Smart Search
- Web Scraping & Data Extraction
- Intelligent Content Summarization
- Error Handling & Recovery Mechanisms
- Streamlit Frontend for easy use

---

## 🌐 Live Website Access
You can try the Web Research Agent directly by visiting the live application at:

Web Research Agent Live

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/web_research_agent.git
cd web_research_agent
```

### 2. Create and Activate Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory and add your Gemini API Key:

```
GEMINI_API_KEY=your_actual_gemini_api_key
```

Or you can directly replace it inside the code if needed.

---

## 🚦 Running the Application

To launch the Streamlit app:

```bash
streamlit run streamlit_app.py
```

This will open the app in your browser automatically!

---

## 🏗 Project Structure

```
web_research_agent/
├── app/
│   ├── agent.py          # Main pipeline orchestration
│   ├── search.py         # Web search functions
│   ├── scraper.py        # Web scraping utilities
│   ├── analyzer.py       # Content summarization and analysis
├── streamlit_app.py      # Streamlit frontend
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
```

---

## ⚙️ Tools Used

- **Web Search Tool**: Simulated search with real API / dummy tool
- **Web Scraper**: BeautifulSoup for content extraction
- **Content Analyzer**: Gemini API for summarization
- **Frontend**: Streamlit

---

## 🧹 Troubleshooting

- **ModuleNotFoundError**: Make sure you have installed all packages using `pip install -r requirements.txt`
- **Google Generative AI Error**: Ensure your API key is valid and `google-generativeai` is installed.
- **Streamlit Deployment Issues**: Double-check `requirements.txt` has all dependencies.

---

## 📽 Demo Video (Loom Link)

[Click here to watch the demo video](https://your-loom-link-here.com)


