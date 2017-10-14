import sqlite3
import csv
from utils import sql
from utils.sql import populate_db

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

populate_db("data/peeps.csv", "peeps", cursor)
populate_db("data/courses.csv", "courses", cursor)

db.commit()

