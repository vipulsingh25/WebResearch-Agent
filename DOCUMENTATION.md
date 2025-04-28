# 📖 Documentation: Web Research Agent

---

## 🧠 Project Overview

The **Web Research Agent** is a simple, modular web app that automates web research:
- **Accepts a user query**
- **Performs a web search** to find related results
- **Scrapes content** from the top webpages
- **Summarizes and analyzes** the collected information
- **Displays a concise research summary** to the user via a **Streamlit frontend**

It combines basic Web Scraping, Web Searching, and LLM-based Content Summarization in one workflow.

---

## ⚙️ How the System Works (Pipeline)

Here's the flow of the system:

```
User Query 
    ↓
Preprocessing (cleaning the query)
    ↓
Web Search (searches web for relevant results)
    ↓
Scraping (extracting textual content from top 5 URLs)
    ↓
Analysis (LLM summarizes extracted text)
    ↓
Final Output (Summary shown on Streamlit UI)
```

---

## 🛠 Detailed Component Breakdown

### 1. **Frontend: `streamlit_app.py`**

- Built with **Streamlit** for quick UI.
- **User enters a query** in a text input field.
- On clicking "Run Research", it **calls** `run_research_pipeline(query)`.
- Displays the final summarized research in a clean, simple layout.

---
  
### 2. **Core Engine: `app/agent.py`**

Responsible for **managing the whole research pipeline**:
- **`preprocess_query(query)`**:  
  Cleans and normalizes the query (e.g., lowercase, strip spaces).

- **`run_research_pipeline(query)`**:  
  Main driver function:
  - Preprocess query.
  - Perform a web search (`perform_search`).
  - Scrape the top 5 search results (`scrape_website`).
  - Analyze all extracted content and create a final summary (`analyze_content`).

Error handling is built-in:
- If no search results are found ➔ returns an appropriate message.
- If scraping fails ➔ alerts the user.

---
  
### 3. **Web Search: `app/search.py`**

- **`perform_search(query)`**:  
  Searches the web based on the user query. 
  (You can either simulate search or plug in a real search API.)
  
- Returns a list of results, each having:
  ```python
  {
    "title": "Page Title",
    "link": "https://example.com"
  }
  ```

---
  
### 4. **Web Scraping: `app/scraper.py`**

- **`scrape_website(url)`**:  
  Scrapes the webpage from the given URL.
- Uses **requests** and **BeautifulSoup** to fetch and parse HTML.
- Extracts main `<p>` tag text contents (paragraphs).
- Cleans up the text to avoid garbage data (e.g., navigation bars, ads).

---
  
### 5. **Content Summarization: `app/analyzer.py`**

- **`analyze_content(scraped_data)`**:  
  Analyzes all scraped contents and produces a concise, structured summary.
- Uses **Google Gemini API** (Generative AI) for intelligent summarization.
- Gives output in easy-to-read bullet points or paragraph form.

---
  
## 🗂 Folder Structure

```
web_research_agent/
├── app/
│   ├── agent.py        # Pipeline management
│   ├── search.py       # Web search functionality
│   ├── scraper.py      # Scraping webpages
│   ├── analyzer.py     # Summarizing content
├── streamlit_app.py    # Streamlit frontend
├── requirements.txt    # Required Python libraries
├── README.md           # Project readme
```

---

## 🧩 Technologies Used

| Purpose        | Technology            |
|----------------|------------------------|
| Frontend       | Streamlit              |
| Web Scraping   | Requests, BeautifulSoup |
| Search Engine  | (Can be real API or dummy) |
| LLM for Summarization | Google Gemini API  |
| Backend        | Python                 |

---

## 🛡 Error Handling

| Scenario | System Behavior |
|----------|-----------------|
| No search results found | Returns ❌ "No search results found." |
| Scraping fails for all pages | Returns ⚠️ "Unable to extract useful information." |
| LLM API failure | Appropriate error handling should be added. |

---

## 📢 Key Notes

- **Environment Variable**:  
  Gemini API Key is expected inside a `.env` file:
  ```
  GEMINI_API_KEY=your_api_key_here
  ```
  
- **Live Deployment**:  
  Host Streamlit on platforms like **Streamlit Cloud**, **Render**, or **AWS EC2** for live access.

- **Customization**:  
  - You can plug in a real web search API (like SerpAPI, Bing API, etc.) in `search.py`.
  - You can swap Gemini with OpenAI GPT, Claude, etc., by updating `analyzer.py`.
