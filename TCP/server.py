from socket import *

serverPort = 1060
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('listening at', serverSocket.getsockname())

connectionSocket, clientAddress = serverSocket.accept()

print('The server now is connected to ', clientAddress)
print('socket connects between', connectionSocket.getsockname(), 'and', connectionSocket.getpeername())

while True:
    sentence = connectionSocket.recv(1024).decode()
    print('Received message from client: ', sentence)

    if sentence == 'Exit':
        print('Reply sent, server socket closed')
        text = 'Disconnect'
        connectionSocket.send(text.encode())
        print('listening at', serverSocket.getsockname())
        break

    else:
        sentenceLength = len(sentence)
        sentenceLength1 = str(sentenceLength)
        connectionSocket.send(sentenceLength1.encode())

connectionSocket.close()
