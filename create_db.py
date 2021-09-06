import sqlite3

# app.create_database()
con = sqlite3.connect("mood.db")

con.execute("create table Timeline(today_date TEXT UNIQUE NOT NULL, mood TEXT NOT NULL, streak_counter INTEGER NOT NULL)")

con.close()