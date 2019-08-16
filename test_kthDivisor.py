import kthDivisor

def test_case1() :
	assert kthDivisor.kthDivisor(63,4) == 9

def test_case2() :
	assert kthDivisor.kthDivisor(5,3) == -1

def test_case3() :
	assert kthDivisor.kthDivisor(100,10) == -1
