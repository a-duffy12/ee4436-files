import time
import statistics as stat
from socket import *

serverName = "localhost"
serverPort = 2806

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

lost = 0

pingTimes = [0,0,0,0,0,0,0,0,0,0]
responseTimes = [0,0,0,0,0,0,0,0,0,0]
rtts = [0,0,0,0,0,0,0,0,0,0]

for i in range(0, 10, 1): # fire 10 pings

    t0 = time.time()
    pingTimes[i] = t0
    msg = "Ping " + str(i+1) + " " + str(t0)

    clientSocket.sendto(msg.encode(), (serverName, serverPort))

    try:
        
        newMsg, serverAddress = clientSocket.recvfrom(2048)
        
        t1 = time.time()
        responseTimes[i] = t1
        print ("\n" + str(serverAddress) + " replied: " + newMsg.decode())

    except timeout:
        print ("\nPacket lost, request timed out")

    rtts[i] = responseTimes[i] - pingTimes[i]
    if rtts[i] > 0:
        print ("Round-trip response time: " + str(rtts[i]*1000) + " ms")
    else:
        lost += 1

rtts = list(filter(lambda a: a>0, rtts))
print ("\nLost " + str(lost) + " packets - " + str(lost*100/10) + "% packet loss rate")

if (len(rtts) > 0):
    print ("\nMinimum RTT: " + str(min(rtts)*1000) + " ms")
    print ("Maximum RTT: " + str(max(rtts)*1000) + " ms")
    print ("Average RTT: " + str(stat.mean(rtts)*1000) + " ms")
    print ("Standard deviation: " + str(stat.stdev(rtts)*1000) +" ms\n")

clientSocket.close()