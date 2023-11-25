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

"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4090"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4080"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4070+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4070"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4060+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+17+-+RTX+4060"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3090+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3090"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3080+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3080"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3070+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3070"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3060+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3060"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+16+-+RTX+3050"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+15+-+RTX+2080"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+15+-+RTX+2060+SUPER"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+05+15+-+RTX+2060"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+04+15+-+GTX+1660+Ti"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+04+15+-+GTX+1660+SUPER"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+04+15+-+GTX+1660"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+04+15+-+GTX+1650+SUPER"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+04+15+-+GTX+1650"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_03+04+15+-+GTX+1630"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+14+-+RX+7900+XTX"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+14+-+RX+7900+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+14+-+RX+7800+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+14+-+RX+7700+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+14+-+RX+7600"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6950+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6900+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6800+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6800"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6750+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6700+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6700"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6650+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6600+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6600"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6500+XT"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+12+-+RX+6400"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+10+-+RX+5700"
"https://?cat=gra16_512&v=e&hloc=at&hloc=de&t=v&sort=p&bl1_id=30&xf=9816_02+04+10+-+RX+5600+XT"

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
