import socket
import sys

amount_or_arg = len(sys.argv)
if amount_or_arg < 2:
    print("Need to have two arguemnts")
elif amount_or_arg==2:
    portnum = sys.argv[1]
    if portnum.isdigit():
            print("Server port is in right format")
            portnum = int(portnum)


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', portnum))
serverSocket.listen(1)
while True:
    connectionSocket , addr = serverSocket.accept()
    tmp = ""
    data = ""
    while (data)!=40:
        tmp= connectionSocket.recv(40)
        if not tmp:
            break
        data+=tmp
connectionSocket.close()
print(data)
quit()