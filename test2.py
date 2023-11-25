import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def scrape_data(url, css_selector):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        selected_elements = soup.select(css_selector)
        
        for element in selected_elements:
            print(element.text.strip())
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}, Content: {response.text}")

# List of URLs to scrape
urls_to_scrape = [
    "https://geizhals.de/?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4080",
    "https://geizhals.de/?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4070+Ti"
]

# CSS selector to extract data
css_selector = "#product0 > div:nth-child(8) > span:nth-child(1) > span:nth-child(1)"

# Loop through each URL and scrape data
for url in urls_to_scrape:
    print(f"Scraping data from: {url}")
    scrape_data(url, css_selector)
    print("\n" + "="*50 + "\n")
