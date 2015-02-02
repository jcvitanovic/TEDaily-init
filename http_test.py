import requests
import json

# https://api.ted.com/v1/talks/1.json?api-key=hzjevu53hy7rggd7w7rnuegf

id = 3
key = 'hzjevu53hy7rggd7w7rnuegf'
param = {'api-key' : key}
url = "https://api.ted.com/v1/talks/" + str(id) + ".json"
r = requests.get(url,params = param)
print(r.url)

with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)

resp_dict = r.json()
print("talk name: "+ resp_dict["talk"]["name"])
print("TAGS: ")
for tag in resp_dict["talk"]["tags"]:
	print(tag["tag"])

print("RATINGS")
#print(resp_dict["talk"]["ratings"])
for k in resp_dict["talk"]["ratings"]:
	print k["rating"]

