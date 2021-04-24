import socket


def receive(the_socket, size):

      #returns the size of in bytes
    return sock.recv(size).decode("utf-8")


def receive_all_data(the_socket, number_of_bytes):
    # send the file we want to receive
    sentFile = file.encode()
    sock.send(sentFile)

    # receive the size of the file and convert to decimal
    acceptSize = sock.recv(40)
    acceptSize = acceptSize.decode()
    acceptSize = int(acceptSize)

    # make a temp. variable to hold the incoming data
    temp = ""
    while(True):
        text = sock.recv(40)
        temp += text.decode()
        if (len(temp) == acceptSize):
            sock.send("1".encode())
            print("THE FILE HAS BEEN ACCEPTED!")
            break

    # open a file path
    path = os.path.join(cliFolder, file)
    data = open(path, "w")
    # write file of recieved data
    data.write(temp)

    # print to notify the user file size and name
    print("The name of the file is: " + file)
    print("The size downloaded is: " + str(acceptSize) + " bytes")

    return 0
