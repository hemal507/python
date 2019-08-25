def appleBoxes(k):
    return sum([x*x for x in range(1,k+1) if x%2 == 0]) - sum([x*x for x in range(1,k+1) if x%2 == 1])


