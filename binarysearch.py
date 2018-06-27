def bsearch(list,num,size):
    lower=0
    upper=size
    found=False
    while lower <= upper:
        mid = (lower + upper)/2
        if num ==list[mid]:
            found=True
            break
        elif num < list[mid]:
            upper=mid-1
        elif num > list[mid]:
            lower=mid+1
    return found,mid

print bsearch([1,2,3,4,6,7,8,9,10,11],5,10)
