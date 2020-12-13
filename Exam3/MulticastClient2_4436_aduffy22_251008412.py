import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # create socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # add ttl to socket

server.bind(("", 2806)) # bind to desired port

req = struct.pack("4sl", socket.inet_aton("224.1.1.1"), socket.INADDR_ANY) # create the structure of the request

server.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req) # add this struct to the socket

while True:
    try:
        data, address = server.recvfrom(1024) # get data from server
        print("Client 2: Data received from: ", (address[0], address[1])) # print data
        print("and the received data is:", data, "\n") # print data
    except:
            print("Timed-out Client 2") # time out error