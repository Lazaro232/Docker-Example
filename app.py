from Database.crud import DatabaseCrud
from Database.connection import DATABASE_INFO

database = DatabaseCrud(DATABASE_INFO)

database.insert_user('LAZARO', 25)
