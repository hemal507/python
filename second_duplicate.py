def firstDuplicate(a) :
	pos = len(a)
	for i in range(len(a)-1) :
		for j in range(i+1,len(a)) :
			if a[i] == a[j] :
				if pos > j :
					pos = j
	if pos == len(a) :
		return -1
	else :
		return a[pos]

import unittest
class TestDups(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(firstDuplicate([2,1,3,5,3,2]),3)
		print('Test case #1 is passed')
        def test_case2(self) :
                self.assertEqual(firstDuplicate([2,2]),2)
                print('Test case #2 is passed') 
        def test_case3(self) :
                self.assertEqual(firstDuplicate([2,4,3,5,1]),-1)
                print('Test case #3 is passed') 	

if __name__ == '__main__':
	unittest.main()
