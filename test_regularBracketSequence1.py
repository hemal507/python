import regularBracketSequence1

def test_case1() :
	assert regularBracketSequence1.regularBracketSequence1("()()") == True

def test_case2() :
	assert regularBracketSequence1.regularBracketSequence1("((())") == False

def test_case3() :
	assert regularBracketSequence1.regularBracketSequence1(")))(((") == False

def test_case4() :
	assert regularBracketSequence1.regularBracketSequence1("())()))") == False

def test_case5() :
	assert regularBracketSequence1.regularBracketSequence1("(((())))()") == True
