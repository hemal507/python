def isLuckyNumber(n):
    for i in str(n) :
        if i != '4' and i != '7' :
            return False
    return True

def isLucky(n) :
	s = str(n)
	fh = s[:len(s)/2]
	fs=0
	for i in fh :
		fs += int(i)
	sh = s[len(s)/2:]
	ss=0
	for j in sh :
		ss += int(j)
	return fs==ss
		

