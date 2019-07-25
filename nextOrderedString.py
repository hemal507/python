d='baca'
d='xy'
from itertools import permutations

def nextOrderedString(d) :
	if len(set(d)) == 1 :
		return 'NO'
	g = set(permutations(''.join(sorted(d))))
	y = []
	for v in g :
		y.append(''.join(v))
	p = sorted(y)
	r='N'
	for i in p :
		if r == 'Y' :
			return i
		if i == d :
			r='Y'

import unittest
class TestNextSort(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(nextOrderedString('baca'),'bcaa')
		print('Test case 1 passed')
	def test_case2(self) :
		self.assertEqual(nextOrderedString('pp'),'NO')
		print('Test case 2 passed')
	def test_case3(self) :
		self.assertEqual(nextOrderedString('xy'),'yx')
		print('Test case 3 passed')

if __name__ == '__main__' :
	unittest.main()
