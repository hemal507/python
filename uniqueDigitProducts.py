def uniqueDigitProducts(a):
    uniq_prod = set()
    for i in a :
        product = 1
        for j in str(i) :
            product *= int(j)
        uniq_prod.add(product)
    return len(uniq_prod)    
                    

import unittest
class TestUniq(unittest.TestCase):
	def test_case1(self) :
		self.assertEqual(uniqueDigitProducts([2, 8, 121, 42, 222, 23]),3)
		print('Test case 1 passed')
	def test_case2(self) :
		self.assertEqual(uniqueDigitProducts([239]),1)
		print('Test case2 passed')
	def test_case3(self) :
		self.assertEqual(uniqueDigitProducts([100,101,111]),2)
		print('Test case 3 passed')

if __name__ == '__main__':
	unittest.main()
