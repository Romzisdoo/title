# I duomenu bazes Naujienu portalu lentele irasom portalus

import sqlite3

conn = sqlite3.connect("inter_cloude.db")
c = conn.cursor()

with conn:
    c.execute("INSERT INTO News_portal VALUES ('NP005', 'vz.lt', 'https://www.vz.lt/')")

# Istrinti irasa
# conn = sqlite3.connect("inter_cloude.db")
# c = conn.cursor()

# with conn:
#     c.execute("DELETE from News_portal WHERE Country_ID='LT001'")

# with conn:
#     c.execute("SELECT * From News_portal")
#     print(c.fetchall())