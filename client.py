import requests

def main():
    print("main")
    server_host = '127.0.0.1'
    server_port = '8080'
    filename = 'HelloWorld.html'
    r = requests.get('http://'+server_host + ':' + server_port + '/' + filename)
    #r = requests.get('https://httpbin.org/')
    print(r.text)

if __name__=='__main__':
    main()