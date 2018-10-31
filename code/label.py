def lab(lat,lon):
	a=[]
	for i in zip(lat,lon):
		a.append(["latitude="+str(i[0]),"longitude="+str(i[1])])
	print(a)
	return a
