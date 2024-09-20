import socket
from datetime import datetime
import os
import pytz
from dotenv import load_dotenv
import requests

HOST = "127.0.0.1"
PORT = 65432
load_dotenv()

# Operation 1: Convert time zone
def convert_timezone(curr_time, from_timezone, to_timezone):
    try:
        #format of date time
        time_format = "%Y-%m-%d %H:%M:%S"
        curr_time_format = datetime.strptime(curr_time, time_format)
        
        # get the from_timezone
        from_tz = pytz.timezone(from_timezone)
        # format from_timezone
        local_time = from_tz.localize(curr_time_format)
        
        # get the to_timezone
        to_tz = pytz.timezone(to_timezone)
        # convert to_timezone
        convert_time = local_time.astimezone(to_tz)
        
        return convert_time.strftime(time_format)
    except Exception as e:
        return f"Error converting time zone: {str(e)}"

# Operation 2: Convert currency
API_KEY = os.getenv('API_KEY')
def convert_currency(money, from_currency, to_currency):
    try:
        money = float(money)
        api_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"
        response = requests.get(api_url)
        data = response.json()
        if response.status_code == 200 and "Realtime Currency Exchange Rate" in data:
            exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
            convert_amount = exchange_rate * money
            return f"{money} {from_currency} is equal to {convert_amount:.2f} {to_currency}"
        else:
            return "Error: Could not retrieve exchange rate data"
    except Exception as e:
        return f"Error converting currency: {str(e)}"

# Process request sent from client
def process_request(request):
    try:
        message = request.decode('utf-8')
        operation, args = message.split(':', 1)
        operation = operation.lower()
        # convert timezone
        if operation == 'timezone':
            curr_time, from_timezone, to_timezone = args.rsplit(':', 2)
            result = convert_timezone(curr_time, from_timezone, to_timezone)
        
        # convert currency
        elif operation == 'currency':
            money, from_currency, to_currency = args.split(':')
            result = convert_currency(money, from_currency, to_currency)
        
        else:
            result = "Unsupported operation, only support currency or timezone"
        return result.encode('utf-8')
    except Exception as e:
        return f"Error sending back to client: {str(e)}".encode('utf-8') 

# Start server
def start_server():
    print("Server starting - listening for connections at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected established with {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received client message: '{data!r}' [{len(data)} bytes]")
                response = process_request(data)
                conn.sendall(response)
                print(f"Sent '{response.decode('utf-8')}' back to client")
    print("Server is done!")

if __name__ == '__main__':
    start_server()