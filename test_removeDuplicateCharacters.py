import removeDuplicateCharacters

def test_case1() :
	assert removeDuplicateCharacters.removeDuplicateCharacters('abdbdczdfdf') == 'acz'

def test_case2() :
	assert removeDuplicateCharacters.removeDuplicateCharacters('abdbdczdfdfacz') == ''
