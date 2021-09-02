from util import time_it

# Dynamic Programming using Memoization Approach

# Fibonacci In Dynamic Programming
# Since the Normal Recursive Call would have to take upto 2 X N recursive it is absolutely slow for Big Numbers
# So we are temporarily declaring the empty hashmap(dictionary) and storing the values and if they repeat we just return the value in the hashmap
def fib(n,memo={}):
	if n in memo:
		return memo[n]
	if n <= 2:
		return 1
	memo[n] = fib(n-1,memo) + fib(n-2,memo)
	return memo[n]

# Grid Traveller Problem
# Here given a 2-Dimensional Array Get a program to traverse from point m to point n
# The Recursive Approach is taken at a point where if any point approaches zero traversing stops or if both point reaches 1 we return 1
# But the same problem as Fibonacci Occurs Here Too Much time is being consumed
# So We have shorted the same using key and storing its value in this key
def gridtraveller(m,n,memo={}):
	key = str(m) + ',' + str(n)
	if key in memo:
		return memo[key]
	if m == 1 and n == 1:
		return 1
	if m == 0 or n == 0:
		return 0
	memo[key] = gridtraveller(m-1, n, memo) + gridtraveller(m, n-1, memo)
	return memo[key]

# CanSum Problem !!!
# The task of the problem is given a number and array of numbers we have to find the possibility if the array of numbers can be added upto the number
# Numbers can repeat here and the output here is boolean
# We can find the number easily by subtracting the numbers from the array with the given number and if it returns zero we can return True else False
# Here to make the large cases faster we have to use Memorization to find the input faster.
# Time Complexity - O(m*n) ; Space Complexity = O(m) ; m= targetsum, n= no if array elements
def canSum(targetsum,numlist,memo={}):
	if targetsum in memo:
		return memo
	if targetsum == 0:
		return True
	if targetsum < 0:
		return False   # We are checking this condition so that the target sum will not go out of bounds
	for num in numlist:
		remainder = targetsum - num
		if canSum(remainder,numlist,memo) == True:
			memo[targetsum] = True
			return True

# 	If nothing is found return false
	memo[targetsum] = False
	return False

# HowSum Problem !!!
# Howsum Problem is same as CanSum problem only exception is that it returns the arrays that match upto the value instead of Boolean Values
# Using Memo to decrease the redundant steps
def howSum(targetsum,elements,memo={}):
	if targetsum in memo:
		return memo[targetsum]
	if targetsum == 0:
		return []
	if targetsum < 0:
		return None
	for element in elements:
		remainder = targetsum - element
		result = howSum(remainder,elements,memo)
		if result != None:
			outputarray = [*result, element]  #Python * equivalent to JavaSscript ...
			memo[element] = outputarray
			return memo[element]
# 	If Not Found
	memo[targetsum] = None
	return None

# Best Sum Problem !!!
# Same as the above CanSum and HowSum problem but the difference we return the shortest possible array
# Using Memo to save some time
def bestSum(targetsum, elements, memo={}):
	if targetsum in memo:
		return memo[targetsum]
	if targetsum == 0:
		return []
	if targetsum < 0:
		return None
	# Defining the shortest solution which takes care of seeing the shortest possible solution
	shortestsolution = None

	for element in elements:
		remainder = targetsum - element
		result = bestSum(remainder,elements,memo)
		if result != None:
			outputarray = [*result, element]  #Python * equivalent to JavaSscript ...
			if shortestsolution == None or len(outputarray) < len(shortestsolution):
				shortestsolution = outputarray

	memo[targetsum] = shortestsolution

	return shortestsolution


if __name__ == '__main__':
	# Printing the Fibonacci Series
	print(fib(100))
	# Printing the GridTraveller Problem
	print(gridtraveller(18, 18))
	# Printing the CanSum Problem
	print(canSum(300, [7, 14]))
	# Printing the HowSum Problem
	print(howSum(300, [7, 3, 5]))
	# Printing Best Sum Problem
	print(bestSum(100, [10, 25, 20]))
