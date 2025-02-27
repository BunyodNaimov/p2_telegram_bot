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
            telegram_id INTEGER UNIQUE,
            is_seller BOOLEAN DEFAULT FALSE,
            full_name CHAR NOT NULL,
            phone_number CHAR NOT NULL,
            age INTEGER NOT NULL,
            address CHAR NOT NULL
            )
            """
        )
    # User Table ga malumot qo'shish
    def add_to_users(self, full_name, phone_number,age, address, telegram_id):
        self.create_user_table()
        self.cursor.execute(
            """
            INSERT INTO users (
            full_name, phone_number, age, address, telegram_id)
            VALUES (?, ?, ?, ?, ?) 
            """, (full_name, phone_number, age, address, telegram_id)
        )
        self.connection.commit()

    def get_telegram_user_from_db(self, telegram_id):
        self.create_user_table()
        user = {}
        db_user = self.cursor.execute("""
        SELECT * FROM users WHERE telegram_id = ?""",
                            (telegram_id,)).fetchone()
        if db_user:
            user["id"] = db_user[0]
            user["telegram_id"] = db_user[1]
            user["is_seller"] = db_user[2]
            user["full_name"] = db_user[3]
            user["phone_number"] = db_user[4]
            user["age"] = db_user[5]
            user["address"] = db_user[6]
            return user
        return None


db = Database()