'''
Given array of integers, find the number of sorted pairs formed by its (different) elements such that the second element in the pair is divisible by the first one.
'''

def divisorsPairs(s):
    return len( [(i,j) for i in s for j in s if i != j and j % i == 0] )

