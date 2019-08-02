def removeDuplicateCharacters(string) :
	return ''.join([x for x in string if string.count(x) == 1  ])

