import sqlite3 

def insert_user(user):
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user.id, user.name))
    conn.commit()
    conn.close()

def insert_order(order):
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (order.user.id, order.total()))
    conn.commit()
    conn.close()