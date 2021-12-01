import json

dict ={'people':[{
	"firstname": "Aswin",
	"rollno": 56,
	"cgpa": 8.6,
	"phonenumber": "9976770500"
}]}
with open("sample4.json", "w") as outfile:
	json.dump(dict, outfile)
inp_1=open('sample4.json')
inp_2 = json.load(inp_1)
for i in inp_2['people']:
	print(i)
