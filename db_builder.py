import sqlite3
import csv
from utils import sql
from utils.sql import populate_table

file_loc = "db/lol.db"
DB_NAME = "lol"
db = sqlite3.connect(file_loc)

cursor = db.cursor()
cursor.execute("""
CREATE TABLE peeps (id INTEGER PRIMARY KEY, age INTEGER, name STRING)
""")

cursor.execute("""
CREATE TABLE courses (code STRING, mark INTEGER, id INTEGER)
""")

populate_table("data/peeps.csv", "peeps", cursor)
populate_table("data/courses.csv", "courses", cursor)

db.commit()
db.close()

