def concatenationsSum(a):
	return sum([int(str(x) + str(y)) for x in a for y in a])


'''
import unittest

class ConcatSum(unittest.TestCase) :
	def test_case1(self):
		self.assertEqual(concatenationsSum([10,2]),1344)
		print('Test case 1 passed')

if __name__ == '__main__' :
	unittest.main()
'''

