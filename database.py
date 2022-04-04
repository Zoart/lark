import sqlite3
from sqlite3 import Error
import os


class Database:
    def __init__(self, ):
        self.dbname = db_name

    def create_db(db_file):
        conn = None
        try:
            conn = sqlite3.connect(f"{db_file}")
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def delete_db(self):
        os.remove(f"{self.databasename}")


if __name__ == '__main__':
    pause_for_now = Database()

    # Database.create_db(r"../testdatabase.db")

