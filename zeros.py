import math
def zeros(n):
    fact = str(math.factorial(n))
    print(fact)
    c = -1 
    while(True) :
        if fact[c:]  == str('0' * (c * -1)) :
            c -= 1
	    print(c)
        else :
	    print(c)
            return ((c+1)*-1)

print(zeros(6))
