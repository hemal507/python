import lastDigitOfAPowerB

def test_case1() :
	assert lastDigitOfAPowerB.lastDigit(2,5) == 2 

def test_case2() :
        assert lastDigitOfAPowerB.lastDigit(100,0) == 1


def test_case3() :
        assert lastDigitOfAPowerB.lastDigit(999999,1000000) == 1


def test_case4() :
        assert lastDigitOfAPowerB.lastDigit(583743,384723) == 7




