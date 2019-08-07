def lastDigit(a, b):
    if b == 1 :
        return a
    if b == 0  or a == 1:
        return 1
    if a == 0 :
        return 0
    
    nb=0
    sb=str(b)
    for i in range(len(sb)) : 
        nb = (nb * 10 + (int)(sb[i])) % 4 
        
    na=int(str(a)[-1])
    if nb%4 == 0 :
        ne=4
    else :
        ne=nb%4
    return pow(na,ne) % 10 
    

