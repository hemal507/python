import eulersTotientFunction

def test_case1() :
	assert eulersTotientFunction.eulersTotientFunction(5) == 4

def test_case2() :
	assert eulersTotientFunction.eulersTotientFunction(49) == 42

def test_case3() :
	assert eulersTotientFunction.eulersTotientFunction(1) == 1
