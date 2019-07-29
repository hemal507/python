def caseUnification(inputString):
    if len([x for x in inputString if x.isupper()]) > len(inputString)/2 :
        return inputString.upper()
    return inputString.lower()
