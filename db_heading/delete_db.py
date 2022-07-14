import sqlite3

conn = sqlite3.connect("inter_cloude.db")
c = conn.cursor()

with conn:
    c.execute("DELETE from All_parsing_result WHERE country_id='102'")

with conn:
    c.execute("SELECT * From All_parsing_result")
    print(c.fetchall())