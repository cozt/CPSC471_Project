import socket


def send_data(sock, data):

      data = data.encode("utf-8")
    sentSize = 0
    while (len(data) > sentSize):
        sentSize += sock.send(data[sentSize:])


def sendAllData(sock):
    file = sock.recv(40)
    file = file.decode()

    # find the file and then store the file
    path = os.path.join(servFolder, file)
    data = open(path)
    # read the contents of the file
    info = data.read()

    # save the size of the content and send it
    acceptLen = str(len(info)).encode()
    sock.send(acceptLen)
    
    # loops repeatedly until everything is sent
    while(True):
        info = info.encode()
        sock.send(info)
        acceptData = sock.recv(40)
        acceptData = acceptData.decode()
        if (acceptData == "1"):
            print("Your file has been sent successfully!")
            break
        # makes sure that content is sent in 0.5sec increments
        time.sleep(.500)
    return 0