import requests
from bs4 import BeautifulSoup

def scrape_data(url, css_selector, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        # Use the provided CSS selector to find the desired elements
        selected_elements = soup.select(css_selector)
        
        # Extract and print the text content of the selected elements
        for element in selected_elements:
            print(element.text.strip())
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

# List of URLs to scrape
urls_to_scrape = [
    "https://geizhals.de/?cat=gra16_512&xf=9816_03+05+17+-+RTX+4080&asuch=&bpmin=&bpmax=&v=e&hloc=at&hloc=de&plz=&dist=&mail=&t=v&sort=p&bl1_id=30",
    "https://geizhals.de/?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4070+Ti"
]

# CSS selector to extract data
css_selector = "#product0 > div:nth-child(8) > span:nth-child(1) > span:nth-child(1)"

# User-Agent header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Loop through each URL and scrape data
for url in urls_to_scrape:
    print(f"Scraping data from: {url}")
    scrape_data(url, css_selector, headers)
    print("\n" + "="*50 + "\n")
