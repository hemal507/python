def digitSum(n):
    return reduce(lambda x,y: x+y,map(lambda x: int(x),str(n)))
