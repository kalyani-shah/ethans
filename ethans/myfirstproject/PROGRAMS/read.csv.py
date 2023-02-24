import csv
abc=open(r'./../DATA/starlit.csv')
csvobj=csv.reader(abc)
for each in csvobj:
    print(each[2])