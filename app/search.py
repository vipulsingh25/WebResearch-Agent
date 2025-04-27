from serpapi import GoogleSearch
import os

SERPAPI_KEY = os.getenv("SERPAPI_KEY") or "REPLACE_WITH_YOUR_KEY"

def perform_search(query):
    print(f"Searching the web for: {query}")
    params = {
        "q": query,
        "api_key": 'c762d4c715296c4aed96927d62b105412756ab29f917aad3281db8f061ba9886',
        "num": 5,
        "engine": "google"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])

        return [
            {"title": r.get("title", "No Title"), "link": r.get("link", "")}
            for r in organic_results if "link" in r
        ]

    except Exception as e:
        print(f"Search API error: {e}")
        return []
