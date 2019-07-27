def factorialTrailingZeros(n) :
	r=0
	f = str(tailRecursionFactorial(n))
	for i in f[::-1] :
		if i == '0' :
			r += 1
		else :
			break
	return r

def tailRecursionFactorial(n) :
	return tailFact(n,1)

def tailFact(number,break_value) :
	if number == 1 :
		return break_value
	return tailFact(number-1 , number * break_value)

