# This files contains other important algorithms

# To find Unit Digit of a number

def findunitdigit(num):
    unitno = num % 10
    return unitno
    
# number of digits in a number

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

#Program to cocatenate two numbers
def numConcat(num1, num2):
  
     # find number of digits in num2
     digits = len(str(num2))
  
     # add zeroes to the end of num1
     num1 = num1 * (10**digits)
  
     # add num2 to num1
     num1 += num2
  
     return num1

# Find the first digit
def firstDigit(n) :
 
    # Remove last digit from number
    # till only one digit is left
    while n >= 10:
        n = n / 10;
     
    # return the first digit
    return int(n)

# Palindrome of two numbers
def isPalindrome(x):
    if x < 0 or x % 10 ==x:
        return False
        
    temp = x
    revnum = 0
    
    while x > 0:
        revnum = revnum * 10 + x % 10
        x = x // 10

    return revnum == temp

# Fibonacci Best Approach
def fibonacci(n):
	a = 0
	b = 1

	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")

	# Check is n is equal
	# to 0
	elif n == 0:
		return 0

	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

# Valid-Sudoku Problem
#we have one 9x9 Sudoku board. We have to check whether that is valid or now. Only the filled cells need to be validated according to the following rules −

#Each row must contain the digits from 1-9 without repetition.
#Each column must contain the digits from 1-9 without repetition.
#Each of the 9 (3x3) sub-boxes of the grid must contain the digits from 1-9 without repetition.

def validsudoku(board):
	#  Watch this video for better undestanding: https://www.youtube.com/watch?v=rJ9NFK9s_mI
	seen = {}

	for i in range(9):
		for j in range(9):
			if board[i][j] != ".":
				keyrow = "Row" + str(i) + str(board[i][j])
				keycol = "Col" + str(j) + str(board[i][j])
				keybox = "Box" + str((i // 3) * 3 + (j // 3)) + str(board[i][j]) # For finding Subboxes condition
				if keyrow not in seen and keycol not in seen and keybox not in seen:
					seen[keyrow] = True
					seen[keycol] = True
					seen[keybox] = True
				else:
					return False
	return True

# Same Thing we are going to but Instead of checking we are going to solve the sudoku Problem
def sudokuSolver(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == ".":
				for k in range(1,10):
					if isValid(board, i, j, k):
						board[i][j] = str(k)

						if (sudokuSolver(board)):
							return True #If it's the solution return true
						else:
							board[i][j] = '.' #Otherwise go back

				return False

	return True
def isValid(board,row,col,key): # ----> Utility function to check if the correct based on the parameters for Sudoku Solver
	for i in range(9):
		# Checking if the number is present in any of the rows or columns or in the sub box
		if board[i][col] != "." and board[i][col] == key:
			return False
		if board[row][i] != "." and board[row][i] == key:
			return False
		if (board[3 * (row // 3) + i // 3][ 3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == key):
			return False

		return True

if __name__ == '__main__':
    # print(findunitdigit(5692))
    # print(countDigit(569))
    # print(numConcat(906, 91))
    # print(firstDigit(569))
    # print(isPalindrome(1122))

    x = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    print(validsudoku(x))
    sudokuSolver(x)
    print(validsudoku(x))
