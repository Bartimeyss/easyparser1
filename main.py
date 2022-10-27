# scraper.py
import requests
from bs4 import BeautifulSoup

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
