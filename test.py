import requests
import concurrent
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as e:
    fs = [e.submit(requests.get, "http://127.0.0.1:8080/HelloWorld.html") for _ in range(50)]
    for f in concurrent.futures.as_completed(fs):
        print(f.result())