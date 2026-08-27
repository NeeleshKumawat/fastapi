from fastapi import FastAPI
import sqlite3

app =FastAPI()

conn = sqlite3.connect('test.db', check_same_thread=False)
curr = conn.cursor()

curr.execute("""
    Create Table if not Exists todos (
        id Integer Primary Key,
        title Text,
        completed Text
    )
""")

conn.commit()

@app.get('/')
def home():
    return {
        "message": "Sqlite Db connected"
    }


