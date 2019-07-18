def mutateTheArray(n, a):
    b = []
    prev,next,curr=0,0,0
    for i in range(n) :
        if i == 0 :
            prev = 0
        else :
            prev = a[i-1]
        if i == len(a) - 1 :
            next = 0
        else :
            next = a[i+1]
        element = prev + a[i] + next
        b.append(element)
    return b 
print(mutateTheArray(5,[4,0,1,-2,3]))

