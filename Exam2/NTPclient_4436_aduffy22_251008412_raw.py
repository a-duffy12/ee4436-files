from socket import *
import struct
import sys
import time

NTP_SERVER = "0.ca.pool.ntp.org"
TIME1970 = 2208988800

def sntp_client():

    data = "\x1b" + 47 * "\0"

    client = socket(AF_INET, SOCK_DGRAM)
    client.sendto(data.encode('utf-8'), (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)

    if data:
        print ("Response received from:", address)
        
        t = struct.unpack("!12I", data)[10]
        t -= TIME1970

        print ("\tTime=%s" % time.ctime(t))

    else:
        print ("Error retreiving response!") 

if __name__ == "__main__":
    sntp_client()