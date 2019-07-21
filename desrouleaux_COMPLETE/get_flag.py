#!/usr/bin/env python

import json

json_data = open('incidents.json')
data = json.load(json_data)
json_data.close()

sourceips = {}
dests_from_source = {}
totalips = {}
dests_for_file = {}

for c in data['tickets']:
	curip = c['src_ip']
	dstip = c['dst_ip']
	filehash = c['file_hash']

	if filehash in dests_for_file:
		if dstip not in dests_for_file[filehash]:
			dests_for_file[filehash].append(dstip)
	else:
		dests_for_file[filehash] = []
		dests_for_file[filehash].append(dstip)
	

	if curip in totalips:
		sourceips[curip] +=1
		totalips[curip] +=1
		if dstip not in dests_from_source[curip]:
			dests_from_source[curip].append(dstip)
	else:
		sourceips[curip] = 1
		dests_from_source[curip] = []
		dests_from_source[curip].append(dstip)
		totalips[curip] = 1

	if dstip in totalips:
		totalips[dstip] +=1
	else:
		totalips[dstip] = 1

# sort on the 2nd field [1] which is the count.
top_ip = sorted(totalips.items(), key=lambda x: x[1], reverse=True)
top_src_ip = sorted(sourceips.items(), key=lambda x: x[1], reverse=True)

# take each destination for each file (which are IPs) and get the length of the number of IPs
dests_per_file = map(lambda x: len(x[1]), dests_for_file.items())




# give me the first value of the first item
print "Top Source IP: " + top_src_ip[0][0]
# Note that the IP asked about changes from time to time...
print "Unique Dests for 13.198.222.191: " + str(len(dests_from_source['13.198.222.191']))
print "Unique Dests Per File Avg: " + str(sum(dests_per_file) / len(dests_per_file))
#print totalips


#	print c['src_ip']
#	print type(c['src_ip'])

#print data

