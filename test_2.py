from bs4 import BeautifulSoup
import urllib.request
import pprint

req = urllib.request.urlopen('https://carrick.ru/')
html_code = req.read()
soup = BeautifulSoup(html_code, 'html.parser')
news = soup.find_all('div', class_='entry-block entry-news-big')
results = []


for item in news:
    dict_tmp = {}
    title = item.find('h2').get_text().strip()
    date_item = item.find('span', class_='entry-data').get_text().strip()
    disc = item.find('div', class_='excerpt-text').get_text().strip()

    results.append({'Заголовок':title, 'Дата':date_item, 'Описание':disc})

pprint.pprint(results)

