# All the important matrix and 2D problems are here
from BinarySearch import binary_search
# Transpose of a matrix -- Here row becomes col and col becomes row
def transpose(matrix):
	row = len(matrix)
	col = len(matrix[0])
	# Here col becomes row and row becomes col
	transpose = [[0 * (1) for _ in range(row)] * (1) for _ in range(col)]
	# SWitching rows to cols
	for i in range(row):
		for j in range(col):
			transpose[j][i] = matrix[i][j]

	return transpose



#Spiral Matrix
def spiralMatrix(n):
	spiral = [[0 for _ in range(n)] for _ in range(n)]
	rs = cs = 0
	re = ce = n - 1
	counter = 1

	while rs <= re and cs <= ce:
		# First Row
		i = cs
		while i <= ce:
			spiral[rs][i] = counter
			counter += 1
			i += 1
		rs += 1
		# LastCol
		i = rs
		while i <= re:
			spiral[i][ce] = counter
			counter += 1
			i += 1
		ce -= 1
		# LastRow
		if rs <= re:
			i = ce
			while i >= cs:
				spiral[re][i] = counter
				counter += 1
				i -= 1
			re -= 1
		# First Col
		if cs <= ce:
			i = re
			while i >= rs:
				spiral[i][cs] = counter
				counter += 1
				i -= 1
			cs += 1

	return spiral

# Rotate a matrix by 90 degree
def rotate(matrix):
	length = len(matrix)

	for i in range(length):
		for j in range(i, length):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	for i in range(length):
		for j in range(length // 2):
			matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length - 1 - j], matrix[i][j]

	return matrix

# Search in a 2D Matrix
# Given a sorted Matrix find the position if not return -1
def searchMatrix(matrix,target):
	if len(matrix) == 0:
		return
	if len(matrix) == 1:
		pos = binary_search(matrix[0],target)
		if pos == -1:
			return [-1,-1]
		else:
			return [0,pos]

	# Find the suspected position
	start = 0
	end = len(matrix) - 1
	while start <= end:
		mid = (start + end) // 2
		# Compare the first matrix
		if matrix[mid][0] == target:
			return True
		elif matrix[mid][0] > target:
			end -= 1
		elif matrix[mid][0] < target:
			start += 1
		else:
			break

	pos = binary_search(matrix[end],target)
	if pos == -1:
		return [-1,-1]
	else:
		return [end,pos]


if __name__ == '__main__':
	print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
	print(spiralMatrix(4))
	print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
	print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],16))