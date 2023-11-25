import requests
from bs4 import BeautifulSoup
import time  # Import the time module

def scrape_data(url, css_selector):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Use the provided CSS selector to find the desired elements
        selected_elements = soup.select(css_selector)
        
        # Extract and print the text content of the selected elements
        for element in selected_elements:
            print(element.text.strip())
    else:
        print(f"Failed to fetch data from {url}")

# Original code to extract links
url = "https://geizhals.de/?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    link_elements = soup.select('tr.xf_tr:nth-child(4) > td:nth-child(3) a')
    extracted_links = [link['href'][2:] for link in link_elements if "NVIDIA+alt" not in link['href']
                       and "AMD+alt" not in link['href']
                       and "Professional" not in link['href']
                       and "Matrox" not in link['href']
                       and "Intel" not in link['href']]
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    extracted_links = []  # Set an empty list if the extraction fails

# CSS selector to extract data
css_selector = "#product0 > div:nth-child(8) > span:nth-child(1) > span:nth-child(1)"

# Loop through each URL and scrape data with a 5-second delay
for url_fragment in extracted_links:
    full_url = "https://geizhals.de/" + url_fragment  # Add the correct scheme and domain
    print(f"Scraping data from: {full_url}")
    
    scrape_data(full_url, css_selector)
    
    # Add a 15-second delay
    time.sleep(5)
    
    print("\n" + "="*50 + "\n")
