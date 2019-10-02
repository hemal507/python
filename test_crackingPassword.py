import crackingPassword

def test_case1() :
	assert crackingPassword.crackingPassword([1, 5, 2],2,3) == ["12",  "15",  "21",  "51"]

def test_case2() :
        assert crackingPassword.crackingPassword([4, 6, 0, 3],4,13) == ["0000",  "0364",  "0403",  "0663",  "3003",  "3406",  "3640",  "3666",  "4004",  "4030",  "4043",  "4303",  "4433",  "4446",  "6006",  "6344",  "6604",  "6630",  "6643"]

def test_case3() :
        assert crackingPassword.crackingPassword([1],4,11) == ["1111"]


def test_case4() :
        assert crackingPassword.crackingPassword([8,9],3,10) == []

def test_case5() :
        assert crackingPassword.crackingPassword([4, 6, 0],1,7) == ["0"]

def test_case6() :
        assert crackingPassword.crackingPassword([3],9,3) == ["333333333"]
