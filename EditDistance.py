
		
def edit_cost(string1, string2, i, j, matrix):
	return edit_distance(string1, string2)


def edit_distance(string1, string2):
	m = len(string1)
	n = len(string2)
	
	table = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
	
	for i in xrange(1, n+1):
		table[i][0] = i
		
	for i in xrange(1, m+1):
		table[0][i] = i
		
	for i in xrange(1, n+1):
		for j in xrange(1, m+1):
			temp=0
			if string2[m] != string1[n]:
				temp=1
			
			table[i][j] = min(table[i-1][j-1]+temp,table[i-1][j],table[i][j-1])
			
	return table[n][m]
	
