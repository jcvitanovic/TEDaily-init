import requests
import json
from time import sleep
# https://api.ted.com/v1/talks/1.json?api-key=hzjevu53hy7rggd7w7rnuegf
total_count = 1912

key = 'hzjevu53hy7rggd7w7rnuegf'
param = {'api-key' : key}
for id in range(total_count+200, total_count+800):		
	url = "https://api.ted.com/v1/talks/" + str(id) + ".json"
	r = requests.get(url,params = param)
	if(r.status_code == 200):
		fileName = 'data' + str(id) + '.txt'
		with open(fileName, 'w') as outfile:
		    json.dump(r.json(), outfile)
	sleep(0.5)
