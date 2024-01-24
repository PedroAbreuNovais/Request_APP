import pyodbc

# Configure this with your Azure database credentials
DATABASE_CONFIG = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': 'your_server',
    'database': 'your_database',
    'username': 'your_username',
    'password': 'your_password'
}

def save_transaction(request_data, response_data):
    conn = pyodbc.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    # Assuming a table structure exists to store these details
    cursor.execute("INSERT INTO transactions (request, response) VALUES (?, ?)", 
                   (str(request_data), str(response_data)))
    conn.commit()
    cursor.close()
    conn.close()
