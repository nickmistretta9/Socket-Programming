from socket import *
serverPort = 5166
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
     connectionSocket, addr = serverSocket.accept()

     command = connectionSocket.recv(1024)
     connectionSocket.send(command)

     userID = connectionSocket.recv(1024)
     connectionSocket.send(userID)	 	

     move= connectionSocket.recv(1024)
     connectionSocket.send(move)
     
     connectionSocket.close()
