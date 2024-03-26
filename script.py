import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    quotes = soup.find_all('span',class_='text')
    authors = soup.find_all('small',class_='author')
    for quote, author in zip(quotes, authors):
        print(f"{quote.get_text()} - {author.get_text()}")

