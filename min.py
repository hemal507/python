A=[1, 3, 6, 4, 1, 2]
B=[1,2,3]
C=[-1,-3]

def pos1(D) :
	for i in range(min(A)-1,max(D)+1) :
		if i not in A :
			if i != 0 :
				return i
			else :	
				return i+1
print(pos1(A))
print(pos1(B))
print(pos1(C))

print('')

def new(d) :
	s=sorted(d)
	print(s)
	for i in range(1,100000) :
		if i not in s :
			return i
print(new(A))
print(new(B))
print(new(C))			
