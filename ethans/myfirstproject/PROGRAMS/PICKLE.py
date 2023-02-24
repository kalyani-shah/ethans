import pickle
data1=['kalyani',101,'IT','MECHANICAL']
outfile=open(r'KBC','wb')
pickle.dump(data1,outfile)
outfile.close()

