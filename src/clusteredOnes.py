r = 5
c = 5
maxcluster = 0
size=0

def getElement(arr, row, col):
	global r
	global c
	if(row>=r or row<0 or col>=c or col <0):
		return 0
	else:
		return arr[row][col]

def maxCluster( arr, i,j):
	global r
	global c
	global maxcluster
	global size
	size = size + 1
	arr[i][j] = 2
	if(size>maxcluster):
		maxcluster = size	
	directions = [ [0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,1],[-1,0],[-1,-1] ]
	for iter in range(len(directions)):
		newi= i + directions[iter][0]
		newj= j + directions[iter][1]
		curr = getElement(arr,newi, newj)
		if(curr == 1):
			maxCluster( arr, newi, newj)

def maxOnes(arr, i,j):
	global r
	global c
	global size
	for i in range(r):
		for j in range(c):
			curr = getElement(arr,i,j)
			if(curr == 1):
				size = 0
				maxCluster( arr, i, j)
	
arr = [ [ 0, 0, 0, 1, 1],
	    [ 0, 1, 0, 0, 0],
	    [ 0, 1, 0, 0, 0],
	    [ 0, 0, 0, 0, 1],
	    [ 0, 1, 1, 1, 1], ]
	  
maxOnes( arr, 0, 0)
print(maxcluster)

