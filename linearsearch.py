def lsearch(list,num):
    i=0
    while i<len(list):
        if list[i] == num:
           return True,i
        else:
            i=i+1
    if i==len(list):
         return False,0

print lsearch([1,23,4,5,7,[1,2],5,6,7,],[1,2])
