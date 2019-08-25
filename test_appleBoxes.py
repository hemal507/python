import appleBoxes

def test_case1() :
	assert appleBoxes.appleBoxes(36) == 666

def test_case2() :
	assert appleBoxes.appleBoxes(12) == 78

def test_case3() :
	assert appleBoxes.appleBoxes(5) == -15

def test_case4() :
	assert appleBoxes.appleBoxes(15) == -120
