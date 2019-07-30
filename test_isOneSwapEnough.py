import isOneSwapEnough

def test_positive_case1() :
	assert isOneSwapEnough.isOneSwapEnough("aabaa") == True

def test_positive_case2() :
        assert isOneSwapEnough.isOneSwapEnough("abab") == True

def test_positive_case3() :
        assert isOneSwapEnough.isOneSwapEnough("aaaba") == True

def test_negative_case1() :
        assert isOneSwapEnough.isOneSwapEnough("aabc") == False

def test_negative_case2() :
        assert isOneSwapEnough.isOneSwapEnough("aaabc") == False

