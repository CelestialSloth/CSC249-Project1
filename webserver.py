# I worked on phase 1-2 of this project with Ramsha
import io
import tempfile
from socket import *
import sys  # In order to terminate the program


# Method adapted from https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
# Primarily copy/paste from code in phase 1 of this assignment
def threaded(connectionSocket):
    while True:
        try:
            message = connectionSocket.recv(1024)  # Receive the request message from the client
            if not message:
                print_lock.release()
                break

            # Extract the path of the requested object from the message
            # The path is the second part of HTTP header, identified by [1]
            # The program would occasionally throw an error here when a machine tried to access
            # something that didn't exist, ie "HelloWorl.html". The current program only catches
            # IOErrors, so I set it to throw one when there's an IndexError.
            try:
                filename = message.split()[1]
            except IndexError:
                raise IOError

            # Because the extracted path of the HTTP request includes
            # a character '\', we read the path from the second character
            f = open(filename[1:])

            outputdata = f.read()  # Store the entire contents of the requested file in a temporary buffer
            f.close()

            # Send one HTTP header line into socket
            # Code found in this stack overflow post: https://stackoverflow.com/questions/8315209/sending-http-headers-with-python
            # TA explained that I needed to add .encode()
            connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:

            # Send response message for file not found
            # The following two lines were found in this Stack Overflow post: https://stackoverflow.com/questions/41852380/how-to-abort-a-python-script-and-return-a-404-error
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
            connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())

            # encode and send the 404 error html file instead
            f = open("404Error.html")
            outputdata = f.read()
            f.close()
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            # Close client socket
            connectionSocket.close()

        except Exception:
            print("something else went wrong")

    #connectionSocket.close()


def Main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # http://127.0.0.1:8080/HelloWorld.html

    # Assign a port number
    # Bind the socket to server address and server port
    # Tell the socket to listen to at most 1 connection at a time
    PORT = 8080  # we were told that 8080 was a standard port
    SERVER = gethostbyname(gethostname())  # Diana showed us this code

    serverSocket.bind((SERVER, PORT))
    serverSocket.listen(5)

    while True:
        # Establish the connection
        print('Ready to serve...')

        connectionSocket, addr = serverSocket.accept() # Set up a new connection from the client

        try:
            message = connectionSocket.recv(1024)  # Receive the request message from the client

            # Extract the path of the requested object from the message
            # The path is the second part of HTTP header, identified by [1]
            # The program would occasionally throw an error here when a machine tried to access
            # something that didn't exist, ie "HelloWorl.html". The current program only catches
            # IOErrors, so I set it to throw one when there's an IndexError.
            try:
                filename = message.split()[1]
            except IndexError:
                raise IOError

            # Because the extracted path of the HTTP request includes
            # a character '\', we read the path from the second character
            f = open(filename[1:])

            outputdata = f.read()  # Store the entire contents of the requested file in a temporary buffer
            f.close()

            # Send one HTTP header line into socket
            # Code found in this stack overflow post: https://stackoverflow.com/questions/8315209/sending-http-headers-with-python
            # TA explained that I needed to add .encode()
            connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:

            # Send response message for file not found
            # The following two lines were found in this Stack Overflow post: https://stackoverflow.com/questions/41852380/how-to-abort-a-python-script-and-return-a-404-error
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
            connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())

            # encode and send the 404 error html file instead
            f = open("404Error.html")
            outputdata = f.read()
            f.close()
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            # Close client socket
            connectionSocket.close()

        except Exception:
            print("something else went wrong")

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == '__main__':
    Main()

