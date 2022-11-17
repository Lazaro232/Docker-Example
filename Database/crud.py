import os

from psycopg2 import connect
from dotenv import load_dotenv


class DatabaseConnection():
    def __init__(self) -> None:
        # Database informations
        load_dotenv()
        # load_dotenv(find_dotenv('Database/database.env'))
        self.host = os.environ.get('DB_HOST')
        self.port = os.environ.get('DB_PORT')
        self.database = os.environ.get('DB_NAME')
        self.username = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')


class DatabaseCrud(DatabaseConnection):
    def __init__(self) -> None:
        super().__init__()
        # Create table if not exists
        self.create_table()

    def start_connection(self) -> connect:
        conn = connect(host=self.host, port=self.port,
                       database=self.database, user=self.username,
                       password=self.password)
        return conn

    def create_table(self) -> None:
        # Starting connection
        connection = self.start_connection()
        cursor = connection.cursor()
        # Query
        query = """CREATE TABLE IF NOT EXISTS users(
                        id SERIAL NOT NULL,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL);"""
        # Executing query
        cursor.execute(query)
        # Commiting and closing connection
        connection.commit()
        connection.close()

    def create_user(self, name: str, age: int) -> None:
        # Starting connection
        connection = self.start_connection()
        cursor = connection.cursor()
        # Query
        query = f"""INSERT INTO users (name, age)
        VALUES ('{name}', {age});"""
        # Executing query
        cursor.execute(query)
        # Commiting and closing connection
        connection.commit()
        connection.close()

    def fetch_user_by_id(self, user_id: int) -> tuple:
        # Starting connection
        connection = self.start_connection()
        cursor = connection.cursor()
        # Query
        query = f"""SELECT * FROM users
                    WHERE id = {user_id};"""
        # Executing query
        cursor.execute(query)
        # Fetching user
        user_info = cursor.fetchone()
        # Closing connection
        connection.close()

        return user_info

    def update_user(self, user_id: int, new_name: str, new_age: int) -> None:
        # Starting connection
        connection = self.start_connection()
        cursor = connection.cursor()
        # Query
        query = f"""UPDATE users
                        SET name = '{new_name}', age = {new_age}
                    WHERE id = {user_id};"""
        # Executing query
        cursor.execute(query)
        # Commiting and closing connection
        connection.commit()
        connection.close()

    def delete_user(self, user_id: int) -> None:
        # Starting connection
        connection = self.start_connection()
        cursor = connection.cursor()
        # Query
        query = f"""DELETE FROM users
                    WHERE id = {user_id};"""
        # Executing query
        cursor.execute(query)
        # Commiting and closing connection
        connection.commit()
        connection.close()
