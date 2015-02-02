import requests
import json

# https://api.ted.com/v1/talks/1.json?api-key=hzjevu53hy7rggd7w7rnuegf


def myprint(d):
  for k, v in d.iteritems():
    if isinstance(v, dict):
      myprint(v)
    else:
      print "{0} : {1}".format(k, v)


id = 1
key = 'hzjevu53hy7rggd7w7rnuegf'
param = {'api-key' : key}
url = "https://api.ted.com/v1/talks/" + str(id) + ".json"
r = requests.get(url,params = param)
print(r.url)

#print(r.json())

with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)