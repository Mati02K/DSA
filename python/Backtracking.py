# Backtracking Algorithm
# Backtracking is a general algorithm for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.

#Permutations Problem
# Find the number of permutations possible for displaying the number in the list
def permute(nums):

	result = []
	if (len(nums) == 1):
		return [nums[:]]

	for i in range(len(nums)):
		n = nums.pop(0)
		perms = permute(nums)

		for perm in perms:
			perm.append(n)

		result.extend(perms)
		nums.append(n)

	return result

# Helping Function to swap string
def swap_string(string,pos1,pos2):
	string = list(string)
	string[pos1],string[pos2] = string[pos2],string[pos1]
	result = "".join(string)
	return result

# Same Permutation Problem But with slight different approach
def permutation(string):
	if len(string) == 1:
		return string
	result = []
	def backtrack(str,left,right):
		if left == right:
			result.append(str)
			return
		for i in range(left,right+1):
			# First swapping based on left index and ith position
			str = swap_string(str,left,i)
			# backtracking to find the solution
			backtrack(str,left+1,right)
			# Returning the normal string back to normal position
			#str = swap_string(str,left,i)

	backtrack(string,0,len(string)-1)
	return result

if __name__ == '__main__':
    print(permute([1,2,3]))
    # print(permute([1,1,2]))
    print(swap_string("Mat",1,2))
    print(permutation("Mat"))