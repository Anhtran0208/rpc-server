Name: Anh Tran
## Overview
This is a Remote Procedure Call (RPC) client-server application that supports 2 operations:
- Converting currency: is used for converting money amount from one currency to another one using data from Alpha Vantage API. 
- Converting timezone: is used for converting current time from one timezone to another one using pytz library from Python

## How to run and test the application
### Set up project environment 
- Clone the project repository
- Navigate to the project directory: cd rpc-server
- Install dependencies: pip install -r requirements.txt
- Create Alpha Vantage API key:
  - Go to 'https://www.alphavantage.co/' and click "Get Free API Key"
  - Follow instructions to get your API key
  - Copy and store generated API key
- Create .env file:
  - Inside the project directory, create .env file
  - Put API_KEY=<your_api_key> inside that file

### Run the server
python3 server.py

### Run the client
- Convert currency: python3 client.py currency <amount> <from_currency> <to_currency>
  - Example: python3 client.py currency 100 USD EUR
  - Expected output: 
    Connection established, sending b'currency:100:USD:EUR'
    Message sent, waiting for reply
    Received response: 100.0 USD is equal to 89.56 EUR
- Convert timezone: python3 client.py timezone <from_timezone> <to_timezone>
  - Example: python3 client.py timezone EST UTC
  - Expected output:
    Client starting - connecting to server at IP 127.0.0.1 and port 65432
    Connection established, sending b'timezone:2024-09-20 18:07:13:EST:UTC'
    Message sent, waiting for reply
    Received response: 2024-09-20 23:07:13

If you have any issues when running application, please contact me via tran36a@mtholyoke.edu.
