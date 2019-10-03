import sumOfDivisors

def test_case1() :
	assert sumOfDivisors.sumOfDivisors(12) == 28

def test_case2() :
        assert sumOfDivisors.sumOfDivisors(1) == 1

def test_case3() :
        assert sumOfDivisors.sumOfDivisors(1000) == 2340

def test_case4() :
        assert sumOfDivisors.sumOfDivisors(239) == 240

def test_case5() :
        assert sumOfDivisors.sumOfDivisors(9999) == 15912

def test_case6() :
        assert sumOfDivisors.sumOfDivisors(10000) == 24211
