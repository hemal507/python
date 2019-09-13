def reversedSumOfDigits(p, n):
        if n == 1 :
                return str(p)
        if p == 0 :
                return "-1"
        if p == 1 :
                return str(pow(10,n-1))
        g=(xrange(pow(10,n-1), pow(10,n)))
	r=pow(10,n-1)
	s=pow(10,n)
        for i in g :
                sum = 0
                for j in str(i) :
                        sum += int(j)
                if sum == p :
                        return str(i)
        return "-1"                


