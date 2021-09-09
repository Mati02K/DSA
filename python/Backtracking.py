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


if __name__ == '__main__':
    print(permute([1,2,3]))