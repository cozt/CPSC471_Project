from socket import *
import ephermeral
import sys
import sendData as sd
import receiveAllData as rAD
import subprocess 


if __name__ == "__main__":

    numOfArguments = len(sys.argv)
    if numOfArguments == 3:
        serverName = sys.argv[1]
        serverPort = sys.argv[2]
        if serverPort.isdigit():
            print("Server port is in right format")
            serverPort = int(serverPort)
        else:
            print("Server port needs to be a digit")

    # Create a socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
    print("trying to connect to server")
    clientSocket.connect((serverName, serverPort))

    userInput = input("ftp> ")

    if userInput.startswith('ls'):
        print("Now printing out the directory")
        # Tell the server we want to perform ls
        subprocess.run('ls',shell = True)
    elif userInput.startswith('get'):
        subprocess.run('get', shell = True)
    elif userInput.startswith('put'):
        subprocess.run('put', shell = True)
    elif userInput.startswith('quit'):
        quit()

    else:
        print("Incorrect invocation. Client should be invoked as: client.py <server machine> <server port>")
        quit()
