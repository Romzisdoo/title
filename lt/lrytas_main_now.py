from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-62b9758c-0bebbd344b7794a83e908761"
  }

source = requests.get('https://www.lrytas.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_ = 'LCategoryBlockMain__column') #row

with open("lrytas_now.csv", "w", encoding="UTF-8", newline='') as failas:

    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Šalies id', 'Šalis', 'Portalo ID', 'Naujienų portalas', 'Kalba', 'Skenavimo laikas', 'Kategorija', 'Tekstas', 'Nuoroda'])
    for blokas in blokai:
        try:
            country_id = "101"
            country = "Lithuania"
            portal_id = "200"
            portal = "Lrytas.lt"
            language = "lt"
            scan_time = datetime.now().replace(second=0, microsecond=0)
            kategorija = "Pradinis puslapis"
            tekstas = blokas.find("h2", class_='LPostContent__title').text.strip()
            link_ = 'https://www.lrytas.lt' + blokas.find('a', class_ = 'LPostMedia').get('href')
            csv_writer.writerow([country_id, country, portal_id, portal, language, scan_time, kategorija, tekstas, link_])
        except:
            pass