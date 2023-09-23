import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")

connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()

query = "SELECT * FROM userdata WHERE name = 'ARPAN MONDAL';"
cursor.execute(query)

rows = cursor.fetchall()

print(rows)
