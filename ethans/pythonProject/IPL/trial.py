import csv
infile = open(r'./../IPL/matches.csv')
csvobj=csv.DictReader(infile)
for each in csvobj:
    print(each)