def fact2(n) :
	facto = 1
	for i in range(1,n+1): 
		facto = facto * i
	return facto
print(fact2(7))
	
def new_fact(n,a) :
	if n == 1 :
		return a
	else :
		return new_fact(n-1, n*a)
print(new_fact(5,1))

def fact(i,a) :
	if i == 0 or i == 1  :
		return a
	else :
		return ( fact( (i-1), (a*i) )  )

print(fact(5,1))

