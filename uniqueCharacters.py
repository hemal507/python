def uniqueCharacters(document):
	return sorted([j for i,j in enumerate(document) if j not in document[0:i]])

print(uniqueCharacters("Todd told Tom to trot to the timber"))
