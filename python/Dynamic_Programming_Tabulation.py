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

# Driver Code
if __name__ == '__main__':
	print(fibonacci(100))
