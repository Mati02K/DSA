# One of the Famous Backtracking algorithm N-Queens Alogorithm
#The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
# The Queens Should not be of same row
# The Queens Should not be of same col
# The Queens Should not be be of same Diagonal

# Algorithm to solve
# Only increment the row from here So that you dont have to check for rows condition
# For Columns and Diagonals Create a set where if you have seen a element save it
# There Are two types of diagonals we are dealing here : # Positive Diagonal( Top to Bottom) and Negative Diagonal (Bottom to Top)
# Here for every positive Diagonal in the square (rows + columns) remains Constant at any instance
# Same for every Negative diagonal in the square (rows- columns) remains Constant at any instance
# Saving instance in set or Hashset and checking instance helps us in finding the solution through backtracking

# For more info use this link : https://youtu.be/Ph95IHmRp5M

def nQueens(n):  # Here N states no of rows in the board of chess
	# Initialize the cols,positivediag,negatdiag as empty
	cols = set()
	positivediag = set() # (r + c)
	negativediag = set() # (r - c)

	ans = [] # Our answer array
	board = [["."] * n for _ in range(n)] # Creating a Chess Board of with just dots

	#  Initialize the backtracking algorithm
	def backtracking(row):
		if row == n:
			# Copying our current board and appending it to the answer board
			copy = ["".join(r) for r in board]
			ans.append(copy)
			return

		for col in range(n):
			if col in cols or (row + col) in positivediag or (row - col) in negativediag:
				#  If we find the column in any of the positive,negative or cols set we are just skipping that column and moving
				continue
			#  If the column is not present in any of the above sets it will come here

			cols.add(col)
			positivediag.add(row + col)
			negativediag.add(row - col)
			board[row][col] = "Q"  # Placing a Queen in that postion

			# Calling the backtracking function for next row
			backtracking(row + 1)

			# If backtracking will not passed the first condition row == n, it will come here below
			cols.remove(col)
			positivediag.remove(row + col)
			negativediag.remove(row - col)
			board[row][col] = "." # Again replacing a dot instead of queen in that position bcoz the solution is no longer feasible

	# We will start backtracking from zero
	backtracking(0)
	return ans


if __name__ == '__main__':
	print(nQueens(4))
