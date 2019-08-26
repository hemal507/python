def regularBracketSequence1(sequence):
    l=0
    for i in sequence :
        if i == '('  :
            l += 1
        else :
            l -= 1
        if   l < 0 :
            return False
    if l == 0 :
        return True
    return False



print(regularBracketSequence1('()()'))
