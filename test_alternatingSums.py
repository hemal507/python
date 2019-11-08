import alternatingSums

def test_case1() :
	assert alternatingSums.alternatingSums([50, 60, 60, 45, 70]) == [180, 105]

def test_case2() :
        assert alternatingSums.alternatingSums([100, 50]) == [100, 50]

def test_case3() :
        assert alternatingSums.alternatingSums([80]) == [80, 0]

def test_case4() :
        assert alternatingSums.alternatingSums([100, 50, 50, 100]) == [150, 150]

def test_case5() :
        assert alternatingSums.alternatingSums([100, 51, 50, 100]) == [150, 151]

