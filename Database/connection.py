import os

from dotenv import load_dotenv, find_dotenv

# Database informations
load_dotenv(find_dotenv('Database/database.env'))
host = os.environ.get('host')
port = os.environ.get('port')
database = os.environ.get('database')
username = os.environ.get('db_username')
password = os.environ.get('password')
# Informations tuple
DATABASE_INFO = (host, port, database, username, password)
