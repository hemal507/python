import twinsScore

def test_case1() :
	assert twinsScore.twinsScore([22, 13, 45, 32],[28, 41, 13, 32]) == [50, 54, 58, 64]

def test_case2() :
        assert twinsScore.twinsScore([0, 0, 0],[100, 100, 100]) == [100, 100, 100]

def test_case3() :
        assert twinsScore.twinsScore([42],[42]) == [84]

def test_case4() :
        assert twinsScore.twinsScore([46, 22, 2, 83, 15, 46, 98],[28, 33, 91, 71, 77, 35, 5]) == [74, 55, 93, 154, 92, 81, 103]
