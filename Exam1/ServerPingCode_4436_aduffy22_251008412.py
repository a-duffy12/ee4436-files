import random
from socket import *

serverPort = 2806 # specify port to listen for udp on

serverSocket = socket(AF_INET, SOCK_DGRAM) # create udp socket
serverSocket.bind(("", serverPort)) # bind socket to this local IP at the specified port

while True: # run indefinitely

    msg, clientAddress = serverSocket.recvfrom(2048) # gets message from socket with max buffer size 2048

    if (random.randint(0, 10) >= 3): # generate a random number and check if it's >= 3
        
        newMsg = msg.decode().upper() # decodes message and capitalizes it
        print (newMsg)
        serverSocket.sendto(newMsg.encode(), clientAddress) # encode message and send it back to client address