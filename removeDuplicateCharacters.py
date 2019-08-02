def removeDuplicateCharacters(string) :
	return ''.join([x for x in string if string.count(x) == 1  ])


'''
def removeDuplicateCharacters(str: String): String = {
    str.filter(i => str.count(_ == i) == 1)
      .mkString("")
}

'''

