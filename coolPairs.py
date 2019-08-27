def coolPairs(a, b):
    uniqueSums = { x+y for x in a for y in b if (x*y) % (x+y) == 0   }
    return len(uniqueSums)


print(coolPairs([4, 5, 6, 7, 8],[8, 9, 10, 11, 12]))

