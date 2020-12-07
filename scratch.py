import requests
import pprint
from bs4 import BeautifulSoup

URL = 'http://www.paulgraham.com/articles.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.select("img + font > a[href]")
results[len(results)-1].get('href')

soup1 = BeautifulSoup(requests.get('http://www.paulgraham.com/' + results[0].get('href')).content, 'html.parser')
results1 = soup1.select("font")
essay = results1[0].get_text(' ')
essay1 = essay.replace('\r\n', ' ')
print(essay1)