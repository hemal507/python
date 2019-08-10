import mexFunction

def test_case1() :
	assert mexFunction.mexFunction([0, 4, 2, 3, 1, 7],3) == 3

def test_case2() :
	assert mexFunction.mexFunction([0, 4, 2, 3, 1, 7],10) == 5
