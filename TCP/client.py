from socket import *

serverIP = '127.0.0.1'
serverPort = 1060

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

while True:
    sentence = input('Enter message to send or type Exit to disconnect:')
    clientSocket.send(sentence.encode())

    sentenceLength = clientSocket.recv(1024).decode()

    if sentenceLength == 'Disconnect':
        print('Received message from Server: ', sentenceLength)
        print('Now you are disconnected from the server')
        break
    else:
        print('Received message from Server: ', 'Your data was', sentenceLength, 'bytes')

clientSocket.close()

