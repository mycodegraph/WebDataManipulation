def sum( sum_arr, i, j):
	if sum_arr[i][j] > 0:
		return sum_arr[i][j]
	m = 0
	sum=0
	for k,v in word_freq_hash.iteritems():
		m+=1	
		if m >= i:
			sum+=v
			if(m==j):
				sum_arr[i][j] = sum
				return sum		
		
			
		
		
def create_optimal_bst(n):
	cost = []
	root = []
	sum_arr = []
	for i in range(0,n+1):
		cost.append([0 for _ in range(0,n+1)])
		root.append([0 for _ in range(0,n+1)])
		sum_arr.append([0 for _ in range(0,n+1)])
	
	s = 1
	for k,v in word_freq_hash.iteritems():
		cost[s][s] = v
		s+=1
		if s== n:
			break
	
	for l in range(2,n+1):
		for i in range(1,n-l+1):
			j = i+l-1
			cost[i][j] = 1000000
			
			for r in range(i,j+1):
				c = cost[i][r-1] if ( i < r ) else 0 + cost[r+1][j] if ( j > r ) else 0 + sum( sum_arr, i, j )
				if c < cost[i][j]:
					cost[i][j] = c
					root[i][j] = r
	
	for row in range(1,n+1):
		for col in range(1,n+1):
			print(str(root[row][col])+" "),
			#print str(cost[row][col])+" "
		print "\n"
			

