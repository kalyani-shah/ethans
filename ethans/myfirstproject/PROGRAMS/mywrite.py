outfile = open(r'./../DATA/s.txt','w')
outfile.write('hey')
outfile.write('\nnonsense')
outfile.flush()
infile = open(r'./../DATA/s.txt','r')
print(infile.read())
outfile.write('you are a good person')
