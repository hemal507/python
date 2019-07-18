def graphEdges(matrix) :
	return len([y for x in matrix for y in x if y == True]) / 2

import unittest
class TestEdgeCount(unittest.TestCase) :
	def test_case1(self) :
		test_matrix1 = [[False,True,True], [True,False,False], [True,False,False]]
		self.assertEqual(graphEdges(test_matrix1),2)
		print('Test case 1 is paased')
        def test_case2(self) :
                test_matrix1 = [[False,False,False], [False,False,False], [False,False,False]]
                self.assertEqual(graphEdges(test_matrix1),0)
                print('Test case 2 is passed')
        def test_case3(self) :
                test_matrix1 = [[False,True,True], [True,False,True], [True,True,False]]
                self.assertEqual(graphEdges(test_matrix1),3)
                print('Test case 3 is passed')

if __name__ == '__main__' :
	unittest.main()

