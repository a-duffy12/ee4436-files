from socket import *
import struct
import sys
import time

NTP_SERVER = "0.ca.pool.ntp.org" # NTP server
TIME1970 = 2208988800 # reference time in seconds since beginning of 1900

def sntp_client(): # function for client

    data = "\x1b" + 47 * "\0" # specific data string

    client = socket(AF_INET, SOCK_DGRAM) # create client
    client.sendto(data.encode('utf-8'), (NTP_SERVER, 123)) # send data to server
    data, address = client.recvfrom(1024) # set response to variables

    if data: # if the response is not empty
        print ("Response received from:", address) # print response
        
        t = struct.unpack("!12I", data)[10] # get the time value from the server
        t -= TIME1970 # time at 1970 from server's response

        print ("\tTime=%s" % time.ctime(t)) # print current time based on number of seconds since 1970

    else: # if the response is blank
        print ("Error retreiving response!") 

if __name__ == "__main__":
    sntp_client() # run main function