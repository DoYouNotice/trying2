import requests
from bs4 import BeautifulSoup

def scrape_data(url, css_selector):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        selected_elements = soup.select(css_selector)

        # Create a list to store the scraped data
        scraped_data = [element.text.strip() for element in selected_elements]

        return scraped_data
    else:
        return f"Failed to fetch data from {url}"

# List of URLs to scrape
urls_to_scrape = [
    "https://geizhals.de/?cat=gra16_512&xf=9816_03+05+17+-+RTX+4080&asuch=&bpmin=&bpmax=&v=e&hloc=at&hloc=de&plz=&dist=&mail=&t=v&sort=p&bl1_id=30",
    "https://geizhals.de/?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4070+Ti"
]

# CSS selector to extract data
css_selector = "#product0 > div:nth-child(8) > span:nth-child(1) > span:nth-child(1)"

# Loop through each URL and scrape data
scraped_results = []
for url in urls_to_scrape:
    print(f"Scraping data from: {url}")
    result = scrape_data(url, css_selector)
    print(result)
    scraped_results.extend(result)
    print("\n" + "=" * 50 + "\n")

# Save the scraped results to a text file
with open("scraped_data.txt", "w") as file:
    for item in scraped_results:
        file.write("%s\n" % item)
