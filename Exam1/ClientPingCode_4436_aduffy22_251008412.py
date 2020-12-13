import time
import statistics as stat
from socket import *

serverName = "localhost"
serverPort = 2806

clientSocket = socket(AF_INET, SOCK_DGRAM) # create udp socket for the server
clientSocket.settimeout(2) # set socket to timeout after 2 seconds

lost = 0 # keep track of lost packets

pingTimes = [0,0,0,0,0,0,0,0,0,0] # list to keep track of ping times
responseTimes = [0,0,0,0,0,0,0,0,0,0] # list to keep track of response times
rtts = [0,0,0,0,0,0,0,0,0,0] # list to keep track of all RTTs

for i in range(0, 10, 1): # fire 10 pings

    t0 = time.time() # get current time
    pingTimes[i] = t0 # store ping time
    msg = "Ping " + str(i+1) + " " + str(t0) # create message

    clientSocket.sendto(msg.encode(), (serverName, serverPort)) # encode message and send it to the specified ip and port

    try: # try to receive a response
        
        newMsg, serverAddress = clientSocket.recvfrom(2048) # get new modified message from socket
        
        t1 = time.time() # get current time
        responseTimes[i] = t1 # store response time
        print ("\n" + str(serverAddress) + " replied: " + newMsg.decode()) # print reply

    except timeout: # if the response was not received
        print ("\nPacket lost, request timed out")

    rtts[i] = responseTimes[i] - pingTimes[i] # calculate RTT
    if rtts[i] > 0:
        print ("Round-trip response time: " + str(rtts[i]*1000) + " ms") # print RTT
    else:
        lost += 1 # increase count of lost packets

rtts = list(filter(lambda a: a>0, rtts)) # filter out zero or negative RTTs as they correspond to lost packets
print ("\nLost " + str(lost) + " packets - " + str(lost*100/10) + "% packet loss rate")

if (len(rtts) > 0): # ensure that there were at least some returned packets
    print ("\nMinimum RTT: " + str(min(rtts)*1000) + " ms") # print minimum time
    print ("Maximum RTT: " + str(max(rtts)*1000) + " ms") # print maximum time
    print ("Average RTT: " + str(stat.mean(rtts)*1000) + " ms") # print average time
    print ("Standard deviation: " + str(stat.stdev(rtts)*1000) +" ms\n") # print standard deviation

clientSocket.close() # close socket