from util import time_it

@time_it
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

if __name__ == '__main__':
	# Printing the Fibonacci Series
	print(fib(100))
	# Printing the GridTraveller Problem
	print(gridtraveller(18, 18))
