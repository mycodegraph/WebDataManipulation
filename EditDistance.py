def _min(a,b,c):
  if(a<=b):
		if(c<=a):
			return c
		else:
			return a
	else:
		if(c<=b):
			return c
		else:
			return b
		
		
def edit_cost(string1, string2, i, j, matrix):
	if(i < 0 or j < 0):
		return 0
	if(matrix[i][j] > 0):
		return matrix[i][j]
	
	val=0
	t=0
	if(string1[i] != string2[j]):
		val = 1
	t = _min(edit_cost(string1, string2, i-1, j-1, matrix),edit_cost(string1, string2, i, j-1, matrix),edit_cost(string1, string2, i-1, j, matrix)) + val
	matrix[i][j] = t
	return matrix[i][j]
		
