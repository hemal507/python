def create2DArray(lengths):
    ret_list = []
    for i in lengths :
        ret_list.append(range(i))
    return ret_list    

def create2DArray2(l):
	return [range(x) for x in l]

import unittest
class TestCreate2DA(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(create2DArray2([1,2,0,4]),[[0], [0, 1], [], [0, 1, 2, 3]])
		print('Test case 1 passed')
        def test_case2(self) :
                self.assertEqual(create2DArray2([]),[])
                print('Test case 2 passed')

if __name__ == '__main__' :
	unittest.main()
