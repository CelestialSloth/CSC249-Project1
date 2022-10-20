import requests
import sys

def main(server_host, server_port, filename):


    website = 'http://'+server_host + ':' + server_port + '/' + filename

    #Found method in https://www.tutorialspoint.com/python_network_programming/python_http_client.htm
    r = requests.get(website)

    print(r.text)

if __name__=='__main__':
    #found in https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    arguments = sys.argv
    if(len(arguments) < 4):
        server_host = '127.0.0.1'
        server_port = '8080'
        filename = 'HelloWorld.html'

    else:
        server_host = arguments[1]
        server_port = arguments[2]
        filename = arguments[3]
    main(server_host, server_port, filename)