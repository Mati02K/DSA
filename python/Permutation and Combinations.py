# Given a number n and k , return all possible combinations of k from N integers
def combination(n,k):
	combinations = []

	# Applying DFS
	def backtrack(start, comb):
		if len(comb) == k:
			combinations.append(comb[::])
			# This return keyword allows us to stop if the finding combination and current combination is equal
			return

		for i in range(start, n + 1):
			# Appending first element and searching for second element
			comb.append(i)
			backtrack(i + 1, comb)
			# Popping that element out of the array --> pops out the last element
			comb.pop()

	backtrack(1, [])
	return combinations

# Given a Array Return all the possible combinations of the array
def permutation(nums):
	result = []

	if (len(nums) == 1):
		return [nums[:]]

	for i in range(len(nums)):
		n = nums.pop(0)
		perms = permutation(nums)

		for perm in perms:
			perm.append(n)

		result.extend(perms)
		nums.append(n)

	return result

if __name__ == '__main__':
	print(combination(4,3))
	print(permutation([1,2,3]))