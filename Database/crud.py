from psycopg2 import connect


class DatabaseCrud():
    def __init__(self, database_info: tuple) -> None:
        # Database informations
        self.host, self.port, self.database, \
            self.username, self.password = database_info
        # Connection timeout
        self.timeout = 40

    def start_connection(self) -> connect:
        conn = connect(host=self.host, port=self.port,
                       database=self.database, user=self.username,
                       password=self.password)
        return conn

    def insert_user(self, name: str, age: int) -> connect:
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


'''
Query to create table

CREATE TABLE users(
    id SERIAL NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL);
'''
