def adjacentElementsProduct(inputArray) :
	return max([ i * j for i , j in zip(inputArray[:-1] , inputArray[1:] ) ])


