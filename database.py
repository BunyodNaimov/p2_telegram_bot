import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("shop.db")
        self.cursor = self.connection.cursor()

    # Users table ni yaratish
    def create_user_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            full_name CHAR NOT NULL,
            phone_number CHAR NOT NULL,
            age INTEGER NOT NULL,
            address CHAR NOT NULL
            )
            """
        )
    # User Table ga malumot qo'shish
    def add_to_users(self, full_name, phone_number,age, address):
        self.create_user_table()
        self.cursor.execute(
            """
            INSERT INTO users (
            full_name, phone_number, age, address)
            """, (full_name, phone_number, age, address)
        )
        self.connection.commit()




db = Database()