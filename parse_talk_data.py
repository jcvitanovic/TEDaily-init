import json


tag_set = set()
tag_dict_count = {}
total_count = 1912
talk_info = []
f = open('talk_overview.txt', 'w+')
f2 = open('just_tags.txt','w+')
for id in range(1, total_count+1):
	fileName = 'talk_data/data' + str(id) + '.txt'	
	with open(fileName) as json_file:
		json_data = json.load(json_file)    
		resp_dict = json_data
		if 'error' in resp_dict:
			continue
		info_line = "ID: %s NAME: %s TAGS " % (unicode(resp_dict["talk"]["id"]), unicode(resp_dict["talk"]["name"]) )
		#info_line += unicode(resp_dict["talk"]["tags"])
		info_line += ', '.join([str(item["tag"]) for item in resp_dict["talk"]["tags"]])
		info_line += '\n'
		f.write(info_line.encode('utf-8'))
		info_line2 = "%s|" % (unicode(resp_dict["talk"]["id"]))
		info_line2 += ','.join([str(item["tag"]) for item in resp_dict["talk"]["tags"]])
		info_line2 += '\n'	
		f2.write(info_line2.encode('utf-8'))	
		for tag in resp_dict["talk"]["tags"]:
			tag_set.add(tag["tag"])
			if tag["tag"] not in tag_dict_count:
				tag_dict_count[tag["tag"]] = 1
			else:
				tag_dict_count[tag["tag"]] += 1
f.close()
f2.close()
print len(tag_set)
with open("tags.txt","w+") as all_tag_file:
	for k,v in sorted(tag_dict_count.items(), key=lambda x:x[1]):
		all_tag_file.write("%s : %s \n" %  (str(k), str(v)))
