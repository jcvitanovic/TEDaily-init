import requests
import json

# https://api.ted.com/v1/talks/1.json?api-key=hzjevu53hy7rggd7w7rnuegf

id = 1
key = 'hzjevu53hy7rggd7w7rnuegf'
param = {'api-key' : key}
url = "https://api.ted.com/v1/talks/" + str(id) + ".json"
r = requests.get(url,params = param)
print(r.url)
#print(r.json())