from socket import *
import sys 
host = '127.0.0.1'
Port=int(sys.argv[1])
clientsocket=socket(AF_INET,SOCK_DGRAM)

clientsocket.bind(('',Port))
message=" ".join(sys.argv[2::])

clientsocket.sendto(message.encode(),(host,12000))
modifiedmessage , serverAddress = clientsocket.recvfrom(2048)
print(f"Message : {modifiedmessage.decode()} ")
clientsocket.close()