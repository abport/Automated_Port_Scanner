
# Automated Port Scanner

This script allows you to automate the process of scanning a host for open ports.

## Requirements
- Python 3 installed on your computer

## How the script works
The script uses the socket library in Python to connect to each port on the specified host. If the connection is successful, the script reports that the port is open. If the connection fails, the script reports that the port is closed.

## How to use the script
1. Open a text editor and copy the code from the code section of this documentation into a new file. Save the file with a `.py` extension, for example `port_scan.py`.
2. Open the terminal or command prompt on your computer.
3. Navigate to the directory where you saved the script file.
4. Run the script by typing `python port_scan.py` in the terminal or command prompt and pressing enter.
5. The script will prompt you to enter the IP address of the host you want to scan.
6. The script will then scan all ports from 1 to 65535 on the specified host and report which ports are open and which are closed.

## Code:
```python
import socket

def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("Port {}: Open".format(port))
        else:
            print("Port {}: Closed".format(port))
        sock.close()
    except socket.gaierror:
        print("Host not reachable")
    except socket.error:
        print("Could not connect to server")

host = input("Enter host IP address: ")
for port in range(1, 65535):
    port_scan(host, port)
```
