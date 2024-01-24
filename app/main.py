import json
from api import call_api
from database import save_data

def main():
    # Dummy data for the API call
    request_data = {
        'customer_id': 538,
        'date': '2021-02-04T19:48:17.000Z',
        'terminal_id': 7,
        'tx_amount': 704.19,
        'tx_id': '4fc665829b61724781c47042ec17f81456dfee3fc20d7f256818e3ee4f44062',
        'tx_payment': 'POS'
    }

    # Call the API
    response_data = call_api(request_data)

    # Convert data to JSON string for storage
    request_json = json.dumps(request_data)
    response_json = json.dumps(response_data)

    # Save request and response data to the database
    save_data('requests', request_json)
    save_data('responses', response_json)

    print("Data saved successfully.")

if __name__ == "__main__":
    main()
