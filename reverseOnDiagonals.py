def reverseOnDiagonals(matrix):
	l=len(matrix)/2
	pos=len(matrix)-1
	for x in range(l) :
		matrix[x][x] , matrix[pos][pos] = matrix[pos][pos] , matrix[x][x]
		pos -= 1
	pos=len(matrix)-1
	for x in range(l) :
		matrix[pos][x] , matrix[x][pos] = matrix[x][pos] , matrix[pos][x]
		pos -= 1	
	return matrix

#print(reverseOnDiagonals([[1,2,3],  [4,5,6],   [7,8,9]]))
print(reverseOnDiagonals( [ [1,2,3,4] , [5,6,7,8] , [9,10,11,12] , [13,14,15,16] ]  ) )

print(reverseOnDiagonals( [[43,455,32,103],  [102,988,298,981],  [309,21,53,64],  [2,22,35,291]] ) ) 

#[[34,1000,139,248,972,584],  [98,1,398,128,762,654],  [33,498,132,543,764,43],  [329,12,54,764,666,213],  [928,109,489,71,837,332],  [93,298,42,53,76,43]] ) )
