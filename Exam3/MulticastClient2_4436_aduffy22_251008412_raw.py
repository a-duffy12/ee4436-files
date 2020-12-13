import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("", 2806))

req = struct.pack("4sl", socket.inet_aton("224.1.1.1"), socket.INADDR_ANY)

server.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)

while True:
    try:
        data, address = server.recvfrom(1024)
        print("Client 2: Data received from: ", (address[0], address[1]))
        print("and the received data is:", data, "\n")
    except:
            print("Timed-out Client 2")