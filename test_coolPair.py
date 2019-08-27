import coolPairs

def test_case1() :
	assert coolPairs.coolPairs([4, 5, 6, 7, 8],[8, 9, 10, 11, 12]) == 2 

def test_case2() :
	assert coolPairs.coolPairs([1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6]) == 4

def test_case3() :
	assert coolPairs.coolPairs([2],[2]) == 1

def test_case4() :
        assert coolPairs.coolPairs([7, 8, 9] , [5, 3, 2]) == 0
