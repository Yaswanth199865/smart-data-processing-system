import sqlite3

def init_db():
    print("INIT DB RUNNING")

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value INTEGER
        )
    ''')

    conn.commit()
    conn.close()


def insert_data(name, value):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO records (name, value) VALUES (?, ?)",
        (name, value)
    )

    conn.commit()
    conn.close()