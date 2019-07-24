def differentSubstringsTrie(inputString):
    s = set()
    for i in range(len(inputString)) :
        for j in range(i+1, len(inputString)+1) :
            s.add(inputString[i:j])
        
    return len(s)

import unittest
class TestDiffStr(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(differentSubstringsTrie("abac"),9)
		print('test case 1 passed')
	def test_case2(self) :
		self.assertEqual(differentSubstringsTrie("abacaba"),21)
		print('test case2 passed')

if __name__ == '__main__' :
	unittest.main()

