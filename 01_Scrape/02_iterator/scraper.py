import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    """Fetches and extracts raw text from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        
        soup = BeautifulSoup(response.text, "html.parser")
        text = ' '.join(p.get_text() for p in soup.find_all("p"))  # Extract paragraph text
        return text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Read URLs from a text file
with open("../01_input/input.txt", "r", encoding="utf-8") as file:
    urls = [url.strip() for url in file.readlines()]

# Scrape text and write to an output file
with open("../03_output/scraped_texts.txt", "w", encoding="utf-8") as f:
    for url in urls:
        text = scrape_text(url)
        if text:
            f.write(f"{text}\n\n")
