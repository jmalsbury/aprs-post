#This is a very simple example, originally provided by 

import sys, time
from socket import *

serverHost = 'second.aprs.net'
serverPort = 20157
password = '12345'
address = 'KI4MTT-1>APRS,TCPIP*:' 
position = '=3349.14N/11153.56W-'
# comment length is supposed to be 0 to 43 char. long-this is 53 char. but it works
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
