def reduceString(a) :
	if len(a) == 0 :
		return a
	if a[0] == a[-1] :
		a=a[1:-1]
		return reduceString(a)
	else :
		return a

import unittest
class TestReduceString(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(reduceString('abacaba'),'')
		print('Test case# 1 is passed')
	def test_case2(self) :
		self.assertEqual(reduceString('12133221'),'1332')
		print('Test case #2 is passed')
if __name__ == '__main__' :
	unittest.main()
