import reversedSumOfDigits

def test_case1() :	
	assert reversedSumOfDigits.reversedSumOfDigits(15, 3) == "159"

def test_case2() :
        assert reversedSumOfDigits.reversedSumOfDigits(30,2) == "-1"

def test_case3() :
        assert reversedSumOfDigits.reversedSumOfDigits(27,5) == "10899"

def test_case4() :
        assert reversedSumOfDigits.reversedSumOfDigits(0,10) == "-1"

def test_case5() :
        assert reversedSumOfDigits.reversedSumOfDigits(1,20) == "10000000000000000000"

def test_case6() :
        assert reversedSumOfDigits.reversedSumOfDigits(0,1) == "0"


