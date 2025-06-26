# import sqlite3
# 
# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()
# 
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     age INTEGER
# )
# """)
# 
# cursor.execute("INSERT INTO users(username, age) VALUES (?, ?)", ("Bob", 19))
# conn.commit()
# 
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)
# 
# conn.close()


import sqlite3

class Database:
    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade INTEGER NOT NULL
            )
            """
        )
        self.connection.commit()

    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()

    def fetch(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


class Student:
    def __init__(self, name, grade, db: Database):
        self.name = name 
        self.grade = grade 
        self.db = db

    def save(self):
        query = "INSERT INTO students(name, grade) VALUES (?, ?)"
        self.db.execute(query, (self.name, self.grade))
    
    @staticmethod
    def get_all(db: Database):
        students = db.fetch("SELECT * FROM students")
        for s in students:
            print(f"ID : {s[0]} name : {s[1]} grade {s[2]}")

    @staticmethod
    def update_grade(db: Database, student_id, new_grade):
        query = "UPDATE students SET grade = ? WHERE id = ?"
        db.execute(query, (new_grade, student_id))

    @staticmethod
    def delete(db: Database, student_id):
        query = "DELETE FROM students WHERE id = ?"
        db.execute(query, (student_id, ))

db = Database()
s1 = Student("Alice", 90, db)
s2 = Student("Bob", 85, db)
s1.save()
s2.save()
print("ALL Students")
Student.get_all(db)

Student.update_grade(db, student_id=2, new_grade=100)

print("All Students ")
Student.get_all(db)

Student.delete(db, student_id=1)

db.close()