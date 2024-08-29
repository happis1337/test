import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            username TEXT NOT NULL,
                            phone_number TEXT NOT NULL)''')
        self.conn.commit()

    def add_user(self, name, username, phone_number):
        self.cursor.execute("INSERT INTO students (name, username, phone_number) VALUES (?, ?, ?)",
                            (name, username, phone_number))
        self.conn.commit()

    def get_user_by_id(self, id):
        self.cursor.execute("SELECT * FROM students WHERE id=?", (id,))
        return self.cursor.fetchone()