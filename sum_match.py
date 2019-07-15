def sum_match(a,total) :
	for i in a :
		for j in a[1:] :
			if i+j == total :
				return(a.index(i),a.index(j))

print(sum_match([2,7,11,15],9) )
print(sum_match([4,5,3,2,1,6,7],12))
