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

source = requests.get('https://www.15min.lt/').text
soup = BeautifulSoup(source, 'html.parser')
stream = soup.find_all('div', class_ = 'item-data')

with open("15min_srautas.csv", "a", encoding="UTF-8", newline='') as failas:

    csv_writer = csv.writer(failas)
    
    for main in stream:
        try:
            country_id = "CR002"
            country = "Lithuania"
            portal_id = "NP_002"
            portal = "15min.lt"
            language = "lt"
            scan_time = datetime.now().replace(second=0, microsecond=0)
            kategorija = "Start page"
            tekstas = main.find('a', class_ = 'title').text.strip()
            link_ = main.find('a', class_ = 'title').get('href')
            csv_writer.writerow([country_id, country, portal_id, portal, language, scan_time, kategorija, tekstas, link_])
        except:
            pass