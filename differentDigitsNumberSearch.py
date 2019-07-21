def differentDigitsNumberSearch(inputArray):
    for i in inputArray :
	non_uniq = 0
        for j in str(i) :
            if str(i).count(j) > 1 :
                non_uniq += 1
	if non_uniq == 0 :
    		return i	
    return -1
	

import unittest
class TestDigitsNumber(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(differentDigitsNumberSearch([22, 111, 101, 124, 33, 30]),124)
		print('Test case 1 is passed')
        def test_case2(self) :
                self.assertEqual(differentDigitsNumberSearch([22, 1111]),-1)
                print('Test case 2 is passed')
if __name__ == '__main__' :
	unittest.main()
