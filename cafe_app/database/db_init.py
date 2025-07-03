import sqlite3

def init_db():
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT 
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        total REAL,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()