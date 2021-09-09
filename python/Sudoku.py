#  This entire file describes resolving sudoku problem

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

#  The below functions are used to solve the Sudoku Puzzle using Backtracking Algorithm
# Not working !!!! Work to do...
# def find_empty(bo):
#     for i in range(len(bo)):
#         for j in range(len(bo[0])):
#             if bo[i][j] == '.':
#                 return (i, j)  # row, col
#
#     return None
#
# def isValid(bo,num,pos):
# 	# Checking the Row
# 	for i in range(len(bo[0])):
# 		if bo[pos[0]][i] == num and pos[1] != i:
# 			return False
# 	# Check the Column
# 	for i in range(len(bo)):
# 		if bo[i][pos[1]] == num and pos[0] != i:
# 			return False
# 	# Checking the Box
# 	box_x = pos[1] // 3
# 	box_y = pos[0] // 3
#
# 	for i in range(box_y * 3, box_y * 3 + 3):
# 		for j in range(box_x * 3, box_x * 3 + 3):
# 			if bo[i][j] == num and (i, j) != pos:
# 				return False
#
# 	return True
#
# # Solving the Sudoku
# def solve(bo):
# 	find = find_empty(bo)
#
# 	if not find:
# 		return True
# 	else:
# 		row,col = find
#
# 	for i in range(1,10):
# 		if isValid(bo, i, (row, col)):
# 			bo[row][col] = str(i)
#
# 			if solve(bo):
# 				return True
#
# 			bo[row][col] = '.'
#
# 	return False


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = str(i)

            if solve(bo):
                return True

            bo[row][col] = '.'

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = int(pos[1]) // 3
    box_y = int(pos[0]) // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == '.':
                return (i, j)  # row, col

    return None



if __name__ == '__main__':
    x = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(validsudoku(x))
    solve(x)
    print(x)
    print(validsudoku(x))

