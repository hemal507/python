a=[7,8,6,5]

def sortBinDec(a) :
	bi = [bin(x)[2:] for x in a]
	s = sorted(bi,key=lambda x : (x.count('1'), int(x,2) ))
	r=[]
	for i in s :
		r.append(int(i,2))
	return r

import unittest

class TestBinary(unittest.TestCase): 
	def test_case1(self) :
		self.assertEqual(sortBinDec([7,8,6,5]),[8,5,6,7])
		print('Test case1 passed')

if __name__ == '__main__' :
	unittest.main()
