from api_handler import call_api
from db_handler import save_transaction

def main():
    # Dummy data for the API call
    data = {
        'customer_id': 538,
        'date': '2021-02-04T19:48:17.000Z',
        'terminal_id': 7,
        'tx_amount': 704.19,
        'tx_id': '4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062',
        'tx_payment': 'POS'
    }

    # Call the API and get the response
    response = call_api(data)

    # Save the request and response to the database
    save_transaction(data, response)

if __name__ == "__main__":
    main()
