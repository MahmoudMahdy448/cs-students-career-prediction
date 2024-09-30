import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_db_connection():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(connection_string)

def execute_query(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_data(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results