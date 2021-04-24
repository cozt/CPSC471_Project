from socket import *
import ephemeral
import sys


from recieveAllData import receive, recieve_all_data 
from sendData import send_data, sendAllData
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

    userInput = input("ftp> ").lower().split()

    if userInput.startswith('ls'):
            send_data(cliSocket, userInput[0])

            # variable for the size of repsonse
            respSize = recieve(cliSocket, header)

            if (respSize == ""):
                print("Failed to revcieve correct response")
            else:
                response = recieve(cliSocket, int(respSize))
                print(response)

    elif userInput.startswith('get'):
                 if (len(userInput) != 2):
                print("Please use: get <FILE NAME> (downloads file from the server)")
            else:
                send_data(cliSocket, userInput[0])
                recieve_all_data(cliSocket, userInput[1])

    elif userInput.startswith('put'):
                if (len(userInput) != 2):
                print("Please use: put <FILE NAME> (uploads file to the server)")
            else:
                send_data(cliSocket, userInput[0])
                putFile(cliSocket, server, userInput[1])

    elif userInput.startswith('quit'):
            send_data(cliSocket, userInput[0])
            cliSocket.close()
            print("The client connection is now closed.")
            break

    else:
        print("Incorrect invocation. Client should be invoked as: client.py <server machine> <server port>")
        quit()
