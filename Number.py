from math import sqrt
def factors(n):  
    fact=[1,n]  
    check=2  
    rootn=sqrt(n)  
    while check<rootn:  
        if n%check==0:  
            fact.append(check)  
            fact.append(n/check)  
        check+=1  
    if rootn==check:  
        fact.append(check)  
        fact.sort()  
    return len(fact)
def checking(i):
    summ=0
    for x in str(i):
        summ+=int(x)
        if int(x)==1 or int(x)==7:
            return 11
    if (int(str(i)[0])+int(str(i)[1]))%2==0:
        return 11
    if int((str(i)[len(str(i))-2]))%2==1:
        return 11
    if int(str(i)[len(str(i))-1])!=len(str(i)):
        return 11
    if factors(i)!=2:
        return 11
    return summ
for i in range(10,1000):
    if checking(i)<=10:
        print(i)
