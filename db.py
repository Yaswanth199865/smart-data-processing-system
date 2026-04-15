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

def get_all_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()

    conn.close()

    return rows

def update_data(record_id, name, value):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE records SET name = ?, value = ? WHERE id = ?",
        (name, value, record_id)
    )

    conn.commit()
    conn.close()

def delete_data(record_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM records WHERE id = ?",
        (record_id,)
    )

    conn.commit()
    conn.close()
