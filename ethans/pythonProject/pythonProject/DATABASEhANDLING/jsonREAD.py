import json
infile=open(r'sample.json')
#print(infile.read())
data=json.load(infile) #csv.reader(infile)
print(data)
print(data['101']['Salary'])