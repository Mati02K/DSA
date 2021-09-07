# This is the file where Dynamic Programming is achieved through Tabulation Process
# Tabulation is about creating a space for the problem and giving it a starting value and doing the logic

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

# Driver Code
if __name__ == '__main__':
	# Printing Fibonacci
	print(fibonacci(100))
	# Printing GridTraveller
	print(gridTraveller(18,18))
