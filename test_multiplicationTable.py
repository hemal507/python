import multiplicationTable

def test_case1() :
	assert multiplicationTable.multiplicationTable(5) == [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

def test_case2() :
        assert multiplicationTable.multiplicationTable(2) == [[1,2],  [2,4]]

def test_case3() :
        assert multiplicationTable.multiplicationTable(4) == [[1,2,3,4],  [2,4,6,8],  [3,6,9,12],  [4,8,12,16]]

