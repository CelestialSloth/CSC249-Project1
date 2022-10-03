import io
import tempfile
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# http://127.0.0.1:8080/HelloWorld.html
# -------------
# Fill in start
# -------------

  # TODO: Assign a port number
  #       Bind the socket to server address and server port
  #       Tell the socket to listen to at most 1 connection at a time
PORT = 8080 #we were told that 8080 was a standard port
SERVER = gethostbyname(gethostname())  #Diana showed us this code

serverSocket.bind((SERVER, PORT))
serverSocket.listen(1)
# -----------
# Fill in end
# -----------

while True:
    
    # Establish the connection
    print('Ready to serve...') 
    
    # -------------
    # Fill in start
    # -------------
    connectionSocket, addr = serverSocket.accept() # TODO: Set up a new connection from the client
    # -----------
    # Fill in end
    # -----------

    try:
        
        # -------------
        # Fill in start
        # -------------
        message = connectionSocket.recv(1024) # TODO: Receive the request message from the client
        # -----------
        # Fill in end
        # -----------
        
        # Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
        #The program would occasionally throw an error here when a machine tried to access
        #something that didn't exist, ie "HelloWorl.html". The current program only catches
        #IOErrors, so I set it to throw one when there's an IndexError.
        try:
            filename = message.split()[1]
        except IndexError:
            raise IOError

        # Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character
        f = open(filename[1:])
        
        # -------------
        # Fill in start
        # -------------

        outputdata = f.read()  # TODO: Store the entire contents of the requested file in a temporary buffer
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------

        # TODO: Send one HTTP header line into socket
        # Code found in this stack overflow post: https://stackoverflow.com/questions/8315209/sending-http-headers-with-python
        # TA explained that I needed to add .encode()
        connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # -------------
        # Fill in start
        # -------------

        # TODO: Send response message for file not found
        # Code found in this Stack Overflow post: https://stackoverflow.com/questions/41852380/how-to-abort-a-python-script-and-return-a-404-error
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())
        connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>'.encode())

        # Close client socket
        connectionSocket.close()
        # -----------
        # Fill in end
        # -----------

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data