# import sqlite3
# 
# conn = sqlite3.connect("db.sqlite3")
# cursor = conn.cursor()
# 
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT
#     );
# """)
# 
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS  orders(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         total REAL,
#         FOREIGN KEY(user_id) REFERENCES users(id)
#     );
# """)
# 
# cursor.executemany("INSERT INTO users (name) VALUES(?)", [
#     ("Aslan",),
#     ("Saimyk",),
#     ("Bob",)
# ])
# 
# cursor.executemany("INSERT INTO orders(user_id, total) VALUES (?,? )", [
#     (1, 50.0),
#     (1, 150.0),
#     (2,200.0),
#     (3, 300.0),
#     (3, 360.0)
# ])
# conn.commit()
# 
# cursor.execute("SELECT COUNT(*) FROM orders")
# print("ВСего заказов", cursor.fetchone()[0])
# 
# cursor.execute("SELECT SUM(total) FROM orders WHERE user_id = 1")
# print("Сумма заказов пользвателя 1 :", cursor.fetchone()[0])
# 
# cursor.execute("""
#     SELECT user_id , COUNT(*) as order_count
#     FROM orders
#     GROUP BY user_id
# """)
# 
# print("Кол- во заказов по пользователям")
# for row in cursor.fetchall():
#     print(f"User {row[0]} -> {row[1]} orders")
# 
# cursor.execute("""
#     SELECT name FROM users
#     WHERE id IN (
#     SELECT user_id FROM orders
#     GROUP BY user_id
#     HAVING COUNT(*) > 1
#     )
# """)
# 
# print("Польщователи с более чем одним заказом")
# for row in cursor.fetchall():
#     print(row[0])
# 
# cursor.execute("""
#     CREATE VIEW user_order_summary AS 
#     SELECT u.id, u.name, COUNT(o.id) as order_count
#     FROM users u
#     LEFT JOIN orders o ON u.id = o.user_id
#     GROUP BY u.id
# """)
# 
# cursor.execute("SELECT * FROM user_order_summary")
# print("VIEW : user_order_summary")
# for row in cursor.fetchall():
#     print(row)


import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS  orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        total REAL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
""")


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod    
    def create(cls, name):
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        return cls(cursor.lastrowid, name)

    @classmethod 
    def get_all(cls):
        cursor.execute("SELECT * FROM users")
        return [cls(*row) for row in cursor.fetchall()]

    def get_orders(self):
        cursor.execute("SELECT * FROM orders WHERE user_id =?", (self.id,))
        return [Order(*row) for row in cursor.fetchall()]

    def total_spent(self):
        cursor.execute("SELECT SUM(TOTAL) FROM orders WHERE user_id = ?", (self.id,))
        result = cursor.fetchall()[0]
        return result

    def __repr__(self):
        return f"<User {self.id} - {self.name}>"

class Order:
    def __init__(self,id,  user_id, total):
        self.id = id
        self.user_id = user_id
        self.total = total

    @classmethod
    def create(cls, user_id, total):
        cursor.execute("INSERT INTO orders(user_id, total) VALUES (?, ?)", (user_id, total))
        conn.commit()
        return cls(cursor.lastrowid, user_id, total)

    def __repr__(self):
        return f"<ORder {self.id} - User {self.user_id} - {self.total}>"

aslan = User.create("Aslan")
saimyk = User.create("Saimyk")
bob = User.create("Bob")

Order.create(aslan.id, 50.0)
Order.create(aslan.id, 250.0)
Order.create(saimyk.id, 150.0)
Order.create(bob.id, 50.0)
Order.create(bob.id, 50.0)

print("ALl ORders")
for user in User.get_all():
    orders = user.get_orders()
    print(f"{user.name}")
    for o in orders:
        print(f"   - {o}")
    print(f"Result: {user.total_spent()}")