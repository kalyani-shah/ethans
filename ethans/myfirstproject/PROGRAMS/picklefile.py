import pickle
infile=open(r'KBC','rb')
abc=pickle.load(infile)
print(abc)
print(abc[3])