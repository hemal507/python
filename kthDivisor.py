def kthDivisor(n, k):
    try :
        return [x for x in range(1,n+1) if n%x == 0][k-1]
    except :
        return -1


