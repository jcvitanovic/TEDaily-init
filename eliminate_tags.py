f = open('tag_selection', 'r')
tag_dict = {}
for line in f:
	l = line.split(':')
	tag_dict[str(l[0].strip())] = True
f2 = open('just_tags.txt','r')
f3 = open('eliminated_tags','w+')
#print tag_dict
counter = 0
empty_tag_videos = []
for line in f2:
	l = line.split('|')
	talk_id = l[0]
	tags = l[1]
	new_tags = []
	for tag in tags.split(','):
		if tag.strip() not in tag_dict:
			continue
		else:
			new_tags.append(tag.strip())
	if len(new_tags) == 0:
		counter += 1
		empty_tag_videos.append((talk_id, tags))
	else:
		wl = "%s " % (unicode(talk_id))
		wl += ', '.join([str(tag) for tag in new_tags])
		wl += '\n'
		f3.write(wl.encode('utf-8'))
f.close()
f2.close()
f3.close()
print counter
print empty_tag_videos




