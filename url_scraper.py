"""
Script för att hämta och spara artiklar från en lista med URL:er.
Använt i projektet 'NPF i Media - En semantisk analys'.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

os.makedirs('data/raw', exist_ok=True)

def scrape_article(url):
    """
    Hämtar och scrapar en artikel från given URL.
    Returnerar en ordbok med URL, titel, innehåll och en framgångsflagga.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Försöker hitta artikelns titel
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else ''
        
        # Hittar artikelinnehållet
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text().strip() for p in paragraphs])
        
        return {
            'url': url,
            'title': title_text,
            'content': content[:5000],  # Begränsa längd
            'success': True
        }
    
    except Exception as e:
        print(f"Fel vid scraping av {url}: {e}")
        return {
            'url': url,
            'title': '',
            'content': '',
            'success': False
        }

def main():
    # Spara URL:er från fil
    try:
        urls_df = pd.read_csv('data/raw/urls_to_scrape.csv')
        urls = urls_df['url'].tolist()
        print(f"Läste {len(urls)} URL:er från filen")
    except FileNotFoundError:
        print("Hittar inte filen data/raw/urls_to_scrape.csv")
        print("Kontrollera att filen finns och ligger i rätt mapp")
        return
    except Exception as e:
        print(f"Fel vid läsning av fil: {e}")
        return
    
    if not urls:
        print("Inga URL:er hittades i filen!")
        return
    
    results = []
    
    for i, url in enumerate(urls, 1):
        print(f"Scrapar artikel {i}/{len(urls)}: {url[:50]}...")
        result = scrape_article(url)
        results.append(result)
        time.sleep(2)  # Var snäll mot servrarna
    
    # Spara resultat
    df = pd.DataFrame(results)
    successful = df[df['success'] == True]
    
    filename = f'data/raw/scraped_articles_{pd.Timestamp.now().strftime("%Y%m%d_%H%M")}.csv'
    successful.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"\nScrapat {len(successful)}/{len(urls)} artiklar")
    print(f"Sparat till {filename}")

if __name__ == "__main__":
    main()