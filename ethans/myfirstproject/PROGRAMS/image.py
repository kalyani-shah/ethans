infile=open(r'./../DATA/image.png','rb')
outfile=open(r'./../DATA/image_back.png','wb')
outfile.write(infile.read())