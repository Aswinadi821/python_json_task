import json
inp_1=open('sample4.json')
inp_2 = json.load(inp_1)
for i in inp_2['people']:
	print(i)
