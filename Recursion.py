def rec(i):
    
    if i<=1:
        return 1
    else:
        return i*rec(i-1)

print rec(1)    
