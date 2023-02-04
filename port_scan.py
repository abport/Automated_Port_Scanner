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
