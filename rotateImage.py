def rotateImage(a) :
	r=[]
	for i in range(len(a)):
		s=[]
		for j in range(len(a)-1,-1,-1) :
			s.append(a[j][i])
		r.append(s)
	return r

