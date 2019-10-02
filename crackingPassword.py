from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [i for i in list( createNumber(i) for i in sorted(list(product(createNumber(digits),repeat=k) ) )  ) if int(i) % d == 0 ]


print(crackingPassword([4, 6, 0, 3] , 4 ,13))

