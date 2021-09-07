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