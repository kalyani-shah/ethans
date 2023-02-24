import json
infile = open(r'sample.json')
data = json.load(infile)  #csv.reader(infile)
print(data)
outfile = open(r'sampleBack.json','w')
json.dump(data,outfile,indent=0)
outfile.close()

