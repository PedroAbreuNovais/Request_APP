import pyodbc
from config import db_config

def get_db_connection():
    conn_str = f'DRIVER={db_config["driver"]};SERVER={db_config["server"]};DATABASE={db_config["database"]};UID={db_config["username"]};PWD={db_config["password"]}'
    return pyodbc.connect(conn_str)

def save_data(table, data):
    query = f"INSERT INTO {table} (data) VALUES (?)"
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, [data])
            conn.commit()
