import uniqueCharacters

def test_case1() :
	assert uniqueCharacters.uniqueCharacters( "Todd told Tom to trot to the timber" ) == [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't']

def test_case2() :
        assert uniqueCharacters.uniqueCharacters("Brilliant, because bacon bites beat bruschetta") == [" ",  ",",  "B",  "a",  "b",  "c",  "e",  "h",  "i", "l",  "n",  "o",  "r",  "s",  "t",  "u"]

def test_case3() :
        assert uniqueCharacters.uniqueCharacters("codefighter fight codefighter with code") == [" ",  "c",  "d",  "e",  "f",  "g",  "h",  "i", "o",  "r",  "t",  "w"]

def test_case4() :
        assert uniqueCharacters.uniqueCharacters("Veni, Vidi, Vici") == [" ",  ",",  "V",  "c",  "d",  "e",  "i",  "n"]
