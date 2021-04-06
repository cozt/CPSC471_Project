import socket
import sys
argumentnum = len(sys.argv)

if argumentnum==3:
    servername= sys.argv[1]
    serverport= sys.argv[2]
    if serverport.isdigit():
        serverport = int(serverport)
    else:
        print("Please enter a digit")

# creating a socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((servername,serverport))
