# This is the file where Dynamic Programming is achieved through Tabulation Process
# Tabulation is about creating a space(table) for the problem and giving it a starting value and doing the logic
# Here we are breaking our problems in sub problems and performing ur logic in the table alone

# Fibonacci Problem
# The Same Fibonacci problem is done by defining the array of n elements and initializing all the elements to zero
# Then in the next step we declare the second element as one and carry the normal fibonacci login (adding the last two elements)

def fibonacci(n):
    #  Creating a empty list of n+1 elements and assigning basic zero value to it.
    table = [0] * (n+1)
    # Initializing the first number to one so that we can perform fibonnaci properly
    table[1] = 1
    # Perform Fibonacci through loop
    i = 1
    while i < n:
        table[i+1] = table[i] + table[i-1]
        i+=1

    return table[n]

# Grid Traveller Problem
# Given a 2D Array we have to find the number of possible ways to reach it
# Since moving is possible in left and bottom directions we are just adding the numbers.
# [1,1] is pre-destinated as 1 as it is possible to travel from one to one and we are going to use it to traverse

def gridTraveller(m, n):
# 	First Create a Table and empty all the elements
#   m--> rows and n--> columns; incrementing by one their size so all situations is checked
    table = [[0] * (n+1) for i in range(m+1)]
# 	Setting the 1,1 position as 1 for traversal
    table[1][1] = 1
    for i in range(0,m+1):
        for j in range(0, n+1):
            current = table[i][j]
            if j+1 <= n:  # This Condition is placed so that it wont go out of bounds in left direction
                table[i][j+1] += current #Adding the left adjacent element
            if i+1 <= m: # This Condition is placed so that it wont go out of bounds in down direction
                table[i+1][j] += current #Adding the below adjacent element

    return table[m][n]

# Cansum Problem
# Given a target sum say if it possible to sum with array of numbers
# Here our table is of size targetsum and starting 0 position is True rest all false
# So we will add all the elements of array to members of the table and the resultant number is stored as True

def canSum(targetsum, numbers):
    table = [False] * (targetsum + 1)
# 	Initialize 0 as True as it is possible to reach from all numbers
    table[0] = True
    # Traversing Until last before element in array
    for i in range(0,len(table)):
        if table[i] == True:
            for num in numbers:
                if (i+num) <= targetsum: # Checking out of bounds condition
                    table[i+num] = True # Setting whatever numbers are true by adding

    return table[targetsum]

# How Sum Problem
# Here also using targetsum+1 as table size and storing the patterns possible for addition
def howSum(targetsum, numbers):
    # Using None as starting attribute
    table = [None] * (targetsum + 1)
    # Declating a empty array in 0th position as it is possible anyhow
    table[0] = []

    for i in range(0,targetsum):
        if table[i] != None:
            for num in numbers:
                if (i+num) < len(table):
                    # Storing the value of the number along with previous number with the number it brought up here
                    table[i+num] = [*table[i], num]  # Python * equivalent to Javascript ...

    return table[targetsum]


# Best Sum Problem
# Same as HowSum but Only the Shortest possible solution should return
# The condition works by comparing the length of two arrays before storing
def bestSum(targetsum,numbers):
    table = [None] * (targetsum + 1)
    table[0] = []

    for i in range(targetsum):
        if table[i] != None:
            for num in numbers:
                if (i+num) < len(table):
                    combination = [*table[i], num]
                    # Checking if the current combination is lesser than previous combination
                    if table[i+num] == None or len(table[i+num]) > len(combination):
                        table[i+num] = combination

    return table[targetsum]

# Maximum Sum of SubArray or Kadane's Algorithm
# Given A array we have to find the maximum sum of subarray without changing any sequence
def maxSubarray(numbers):
# 	Initialize max as first element as we start from there
    max = numbers[0]
    currentmax = 0
    for num in numbers:
        #  Adding the subarray
        currentmax = currentmax + num
        # If the currentsub array  is maximum make it as max
        if currentmax > max:
            max = currentmax
        # If the value falls below zero make it as zero
        if currentmax < 0:
            currentmax = 0
    return max

# These problem work is bit complicated look into video for understanding
def canConstruct(targetword,words):
    table = [False] * (len(targetword) + 1)
    table[0] = True

    for i in range(len(targetword)+1):
        if table[i] == True:
            for word in words:
                if targetword[i:(i+len(word))] == word:
                    table[i + len(word)] = True

    return table[len(targetword)]

def countConstruct(targetword,words):
    table = [0] * (len(targetword) + 1)
    table[0] = 1

    for i in range(len(targetword) + 1):
        for word in words:
            if targetword[i:(i + len(word))] == word:
                table[i + len(word)] += table[i]

    return table[len(targetword)]

def allConstruct(targetword,words):
    #  Creating [] for all target.length spaces
    table = [[] * (1) for i in range(len(targetword)+1)]
    table[0] = [[]]

    for i in range(len(table)):
        for word in words:
            if targetword[i:(i + len(word))] == word:
                # newcombination = [*table[i], word]
                newcombination =  table[i] + [word]
                table[i+len(word)].append(newcombination)

    return table[len(targetword)]

# Minimum Cost Path
# Given a array of dimension m x n write a program to traverse from top left to bottom right in minimum cost. (Only move in right and bottom)
# Just add the first row and first column and then check down and right and apply the minimum
# https://www.youtube.com/watch?v=lBRtnuxg-gU
def minPathSum(grid):
    row = len(grid)
    col = len(grid[0])
    board = grid
    # First column
    for c in range(1, col):
        board[0][c] = board[0][c - 1] + grid[0][c]
    # First Row
    for r in range(1, row):
        board[r][0] = board[r - 1][0] + grid[r][0]
    # Rest of the rows and cols
    for i in range(1, row):
        for j in range(1, col):
            down = board[i - 1][j] + grid[i][j]
            side = board[i][j - 1] + grid[i][j]
            board[i][j] = min(down, side)

    return board[row - 1][col - 1]

# Program to find the maximum product of a continuous subarray

def maxProduct(nums):
    res = nums[0]
    curMax, curMin = 1, 1 # TO make sure when we meet negative numbers we know where to proceed

    for num in nums:
        tmp = curMax * num
        curMax = max(tmp, curMin * num, num)
        curMin = min(tmp, curMin * num, num)
        res = max(res, curMax)

    return res


# Driver Code
if __name__ == '__main__':
    # Printing Fibonacci
    print(fibonacci(100))
    # Printing GridTraveller
    print(gridTraveller(18,18))
    # Printing Cansum
    print(canSum(13, [3,11]))
    # Printing Howsum
    print(howSum(25,[20,5,10]))
    # Printing BestSum
    print(bestSum(1000, [20, 5, 10, 25]))
    # printing maxsubarry
    print(maxSubarray([5,4,-1,7,8]))
    # Printing CanConstruct
    print(canConstruct("abcdef", ['a','ab','abcd','ef']))
    # Printing CountConstruct
    print(countConstruct("abcdef", ['a','ab','cd','abcd','ef','bcd']))
    # Print all construct
    print(allConstruct('purple',['purp','le','ur','p','purpl']))
    # Print Minsum
    print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    # Printing Maximum SUbarray sum
    print(maxProduct([2, -5, -2, -4, 3]))
