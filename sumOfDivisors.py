def sumOfDivisors(n):
    return sum([x for x in range(1,n+1) if n % x == 0])

print(sumOfDivisors(50000000))
