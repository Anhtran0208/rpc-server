<p> Name: Anh Tran </p> 
<p>Project 1: CSC 249: Computer Networks - Fall 2024</p> 
<h2>Overview</h2>
<p>
  This is a Remote Procedure Call (RPC) client-server application that supports 2 operations:
  <ul>
    <li>
      Converting currency: is used for converting money amount from one currency to another one using data from Alpha Vantage API. 
    </li>
    <li>
      Converting timezone: is used for converting current time from one timezone to another one using pytz library from Python
    </li>
  </ul>
</p>
<h2> How to run and test the application </h2>
<h3>Set up project environment </h3>  
<ul>
  <li> Clone the project repository</li>
  <li>Navigate to the project directory: <b> cd rpc-server </b></li>
  <li>Install dependencies: <b>pip install -r requirements.txt</b> </li>
  <li>
    Create Alpha Vantage API key:
    <ul>
      <li> Go to <b> https://www.alphavantage.co/ </b> and click "Get Free API Key" </li>
      <li> Follow instructions to get your API key </li>
      <li>Copy and store generated API key </li>
    </ul>
  </li>
  <li> 
    Create .env file 
    <ul> 
      <li> Inside the project directory, create .env file </li>
      <li> Put API_KEY=<your_api_key> inside that file </li>
    </ul>
  </li>
</ul>

### Run the server
python3 server.py

### Run the client
- Convert currency: python3 client.py currency <amount> <from_currency> <to_currency>
  - Example: python3 client.py currency 100 USD EUR
  - Expected output: 
    - Connection established, sending b'currency:100:USD:EUR'
    - Message sent, waiting for reply
    - Received response: 100.0 USD is equal to 89.56 EUR
- Convert timezone: python3 client.py timezone <from_timezone> <to_timezone>
  - Example: python3 client.py timezone EST UTC
  - Expected output:
    - Client starting - connecting to server at IP 127.0.0.1 and port 65432
    - Connection established, sending b'timezone:2024-09-20 18:07:13:EST:UTC'
    - Message sent, waiting for reply
    - Received response: 2024-09-20 23:07:13

If you have any issues when running application, please contact me via tran36a@mtholyoke.edu.
