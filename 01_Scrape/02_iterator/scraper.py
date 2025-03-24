import requests
from bs4 import BeautifulSoup

def scrape_websites(input_file, output_file):
    with open(input_file, "r") as file:
        urls = file.readlines()
    
    with open(output_file, "w", encoding="utf-8") as out:
        for url in urls:
            url = url.strip()
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")
                text = soup.get_text(separator=" ").strip()
                out.write(f"URL: {url}\n{text}\n\n")
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

# Usage
scrape_websites("input.txt", "scraped_text.txt")
