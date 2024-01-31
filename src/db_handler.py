import pyodbc

# Configure this with your Azure database credentials
DATABASE_CONFIG = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': 'ccfdb.database.windows.net',
    'database': 'ccfdb',
    'username': 'adminpedro',
    'password': '9UAUGKqz=oF;T38wJNKj'
}


def check_or_create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='transactions' AND xtype='U'
            )
            CREATE TABLE transactions (
                id INT PRIMARY KEY IDENTITY,
                request NVARCHAR(MAX),
                response NVARCHAR(MAX)
            )
        """)
        cursor.commit()

def save_transaction(request_data, response_data):
    connection = pyodbc.connect(**DATABASE_CONFIG)
    
    # Check if table exists, if not, create it
    check_or_create_table(connection)
    
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO transactions (request, response) VALUES (?, ?)", (str(request_data), str(response_data)))
        connection.commit()
    
    connection.close()
