import requests
import sys

url = sys.argv[2]
wordlist = sys.argv[1] 
with open(wordlist, 'r') as f:
    for line in f:
        r = requests.get(url + line)
        if r.status_code < 400:
            print(url + line)
