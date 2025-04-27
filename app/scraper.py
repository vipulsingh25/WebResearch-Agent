# import requests
# from bs4 import BeautifulSoup

# def scrape_website(url):
#     try:
#         response = requests.get(url, timeout=5)
#         if response.status_code != 200:
#             print(f"Failed to fetch {url} (status code: {response.status_code})")
#             return None

#         soup = BeautifulSoup(response.text, 'html.parser')
#         paragraphs = soup.find_all('p')
#         text = '\n'.join(p.get_text() for p in paragraphs if len(p.get_text()) > 50)

#         return text[:3000]  # Limit to ~3000 chars to control GPT input size

#     except Exception as e:
#         print(f"Error scraping {url}: {e}")
#         return None


import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WebResearchBot/1.0; +https://example.com/bot)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=8)
        if response.status_code != 200:
            print(f"Failed to fetch {url} (status code: {response.status_code})")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove common unwanted elements
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'noscript']):
            tag.decompose()

        paragraphs = soup.find_all('p')
        clean_text = '\n'.join(p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50)

        return clean_text[:3000]  # Keep size reasonable for LLM input

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None
