from itertools import permutations

def rockPaperScissors(players):
    return sorted(permutations(players,2),key=lambda x : (x[0],x[1]))

