'''
given string find the longest substring without repeating characters 
'''
def len_str(inp_str) :
	prev,return_str = '',''
	for i in inp_str :
		if i not in return_str :
			return_str += i
		else :
			if len(prev) < len(return_str) :
				prev = return_str
			return_str = i
	return len(prev), prev

import unittest
class TestSubStrLen(unittest.TestCase) :
	def test_string1(self) :
		self.assertEqual(len_str('abcabcbb'),(3,'abc'))
		print('Test case 1 passed')
	def test_string2(self) :
		self.assertEqual(len_str('bbbbbb'),(1,'b'))
		print('Test case 2 passed')
	def test_string3(self) :
		self.assertEqual(len_str('pwwkew'),(3,'wke'))
		print('Test case 3 passed')
if __name__ == '__main__' :
	unittest.main()
