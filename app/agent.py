# app/agent.py
from app.search import perform_search
from app.scraper import scrape_website
from app.analyzer import analyze_content

def preprocess_query(query: str) -> str:
    """Preprocess user query for search optimization."""
    return query.strip().lower()

def run_research_pipeline(query: str) -> str:
    print("[Agent] Analyzing query...")
    processed_query = preprocess_query(query)

    print("[Agent] Performing web search...")
    results = perform_search(processed_query)

    if not results:
        return "❌ No search results found. Please refine your query."

    scraped_data = []
    for result in results[:5]:
        url = result.get("link", "")
        print(f"[Agent] Scraping: {url}")
        content = scrape_website(url)
        if content:
            scraped_data.append({
                "url": url,
                "title": result.get("title", "Untitled"),
                "content": content
            })

    if not scraped_data:
        return "⚠️ Unable to extract useful information from the search results."

    print("[Agent] Analyzing and synthesizing content...")
    summary = analyze_content(scraped_data)

    return summary
