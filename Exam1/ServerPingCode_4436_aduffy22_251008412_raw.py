import random
from socket import *

serverPort = 2806

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

while True:

    msg, clientAddress = serverSocket.recvfrom(2048)

    if (random.randint(0, 10) >= 3):
        
        newMsg = msg.decode().upper()
        print (newMsg)
        serverSocket.sendto(newMsg.encode(), clientAddress)