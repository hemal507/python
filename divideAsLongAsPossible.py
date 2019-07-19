def divideAsLongAsPossible2(n, d):
    while n % d == 0:
        n //= d
    return n

def divideAsLongAsPossible(n, d):
    if n % d != 0 :
        return n
    if n % d == 0 :
        return divideAsLongAsPossible(n/d, d) 

import unittest
class TestDivPossible(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(divideAsLongAsPossible(64,4),1)
		print('Test case 1 passed')
        def test_case2(self) :
                self.assertEqual(divideAsLongAsPossible(36,3),4)
                print('Test case 2 passed')
        def test_case3(self) :
                self.assertEqual(divideAsLongAsPossible(20,2),5)
                print('Test case 3 passed')

if __name__ == '__main__' :
	unittest.main()
