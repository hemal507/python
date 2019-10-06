import groupDating

def test_case1() :
	assert groupDating.groupDating([5, 28, 14, 99, 17],[5, 14, 28, 99, 16]) == [[28,14,17],  [14,28,16]]

def test_case2() :
        assert groupDating.groupDating([6, 23, 82],[82, 56, 92]) == [[6,23,82],  [82,56,92]]

def test_case3() :
        assert groupDating.groupDating([42], [64]) == [[42],  [64]]

def test_case4() :
        assert groupDating.groupDating([1, 2, 3, 4], [1, 2, 3, 4]) == [ [] ,[] ]


def test_case5() :
        assert groupDating.groupDating([0, 34, 100, 81, 100, 82, 0],[46, 34, 100, 76, 20, 82, 44]) == [[0,81,100,0],  [46,76,20,44]]
