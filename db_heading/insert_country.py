# I duomenu bazes valstybiu lentele irasom valstybes

import sqlite3

conn = sqlite3.connect("inter_cloude.db")
c = conn.cursor()

with conn:
    c.execute("INSERT INTO Country VALUES ('CR006', 'Russia')")

# Istrinti irasa
# conn = sqlite3.connect("inter_cloude.db")
# c = conn.cursor()

# with conn:
#     c.execute("DELETE from Country WHERE Country_ID='LT001'")

# with conn:
#     c.execute("SELECT * From Country")
#     print(c.fetchall())