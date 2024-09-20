import socket
import sys
from datetime import datetime

HOST = "127.0.0.1"
PORT = 65432
# Send request to server
def send_request(operation, args):
    return f"{operation}:{':'.join(args)}".encode('utf-8')

# Start client
def start_client(operation, args):
    print("Client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = send_request(operation, args)
        print (f"Connection established, sending {request}")
        s.sendall(request)
        print("Message sent, waiting for reply")
        data = s.recv(1024)
        print(f"Received response: {data.decode('utf-8')}")
if __name__ == '__main__':
    operation = sys.argv[1].lower()
    
    if operation == 'timezone':
        from_timezone, to_timezone = sys.argv[2], sys.argv[3]
        curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        args = [curr_time, from_timezone, to_timezone]
        
    elif operation == 'currency':
        money, from_currency, to_currency = sys.argv[2], sys.argv[3], sys.argv[4]
        args = [money, from_currency, to_currency]
        
    else:
        print("Unsupported operation, only support currency or timezone")
        sys.exit(1)
    start_client(operation, args)
    