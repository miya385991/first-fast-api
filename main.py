import sqlite3
from fastapi import FastAPI


def create_tebles():
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute(
        'CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    conn.commit()
    conn.close()



app = FastAPI()
def get_db():
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM users')
    users = curs.fetchall()
    conn.close()
    return users


@app.get("/")
def read_root():
    user = {}
    users = get_db()
    for id, name in users:
        user[id] = name
    return user


@app.post('/')
def post_name(name: str):
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    db_text = f'INSERT INTO users(name) values("{name}")'
    curs.execute(db_text)
    conn.commit()
    conn.close()



