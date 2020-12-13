import socket
import time

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # create a socket
soc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) # set up socket with TTL of 255

while True: 
    soc.sendto(b"Multicasting Assignment ECE 4436 from Server 2", ("224.1.1.1", 2806)) # send message
    print("Server 2: Multicast packet is sent now!") # print that message was sent
    time.sleep(3) # sleep for 3 seconds
