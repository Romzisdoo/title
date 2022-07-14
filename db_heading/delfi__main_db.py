from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import sqlite3

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-62b9758c-0bebbd344b7794a83e908761"
  }

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
stream = soup.find_all('div', class_ = 'headline')

conn = sqlite3.connect("inter_cloude.db")
c = conn.cursor()

with conn:
   
    for main in stream:
        try:
            country_id = "CR001"
            country = "Lithuania"
            portal_id = "NP_001"
            portal = "Delfi.lt"
            language = "lt"
            scan_time = datetime.now().replace(second=0, microsecond=0)
            kategorija = main.find('div', class_ = 'headline-category').text.strip()
            tekstas = main.find('a', class_ = 'CBarticleTitle').text.strip()
            link_ = main.find('a', class_ = 'CBarticleTitle').get('href')
            
            c.execute("""
                INSERT INTO All_parsing_result 
                (<Country_ID>, <Country>, <Portal_ID>, <Daily_News_Portal>, <Language>, <Scaning_time>, <Publication_category>, <Heading>, <Publication_link>)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (country, portal_id, portal, language, scan_time, kategorija, tekstas, link_))

            conn.commit()
          
        except:
            pass