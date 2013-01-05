#This is a very simple example
#while loop connects to APRS server, and uploads position packet
#Slight modifications to original code provided by Pete Loveall AE5PL
#Source: http://www.tapr.org/pipermail/aprssig/2007-April/018541.html

#NOTE: change callsigns and passwords for your own use.  

#See readme for links to wiki that discuss getting a password


import sys, time
from socket import *

serverHost = 'second.aprs.net'
serverPort = 20157
password = '12345'
address = 'KI4MTT-1>APRS,TCPIP*:' 
position = '=3349.14N/11153.56W-'
# comment length is supposed to be 0 to 43 char. 
comment = 'KI4MTT Python Script'
packet = ''
delay = 15 # delay in seconds - 15 sec. is for testing- should be 20 to 30 min for fixed QTH

def send_packet():
        # create socket & connect to server
        sSock = socket(AF_INET, SOCK_STREAM)
        sSock.connect((serverHost, serverPort))
        # logon
        sSock.send('user KI4MTT pass ' + password + ' vers "KI4MTT Python" \n')
        # send packet
        sSock.send(address + position + comment +'\n')
        print("packet sent: " + time.ctime() )
        # close socket -- must be closed to avoidbuffer overflow
        time.sleep(15) # 15 sec. delay
        sSock.shutdown(0)
        sSock.close()

packet = address + position + comment
print (packet) # prints the packet being sent
print (len(comment)) # prints the length of the comment part of the packet
while 1:
        send_packet()
        time.sleep(delay)
