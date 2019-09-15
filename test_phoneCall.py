import phoneCall

def test_case1() :
	assert phoneCall.phoneCall(3,1,2,20) == 14

def test_case2() :
	assert phoneCall.phoneCall(2,2,1,2) == 1

def test_case3() :
	assert phoneCall.phoneCall(10,1,2,22) == 11

def test_case4() :
	assert phoneCall.phoneCall(1,2,1,6) == 3

