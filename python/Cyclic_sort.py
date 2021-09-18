# Cycle Sort is a algorithm which you should use when they give you the term 1 - N
# Here all the elements are sorted in from 0,1,2 - N in ascending order
# Time complexity - O(N) but wont work if the order is changed

def cyclic_sort(nums):
	i = 0
	while i < len(nums):
		# correct = nums[i] #  ---> if zero is  included in the list
		correct = nums[i] - 1 #---> if zero is not included in the list
		if nums[i] < len(nums) and nums[i] != nums[correct]:
			nums[i], nums[correct] = nums[correct], nums[i]
		else:
			i += 1
	return nums

# Given a Array from Numbers 1- N find the missing number
# 268. Missing Number --> Leetcode
def missingNumber(nums):
	nums = cyclic_sort(nums)
	for i in range(len(nums)):
		if i != nums[i]:
			return i

	return len(nums)

# Find all the duplicates in the array in range 1-N
#Leetcode question https://leetcode.com/problems/find-all-duplicates-in-an-array/
def findDuplicates(nums):
	i = 0
	while i < len(nums):
		correct = nums[i] - 1
		if nums[i] != nums[correct]:
			nums[i], nums[correct] = nums[correct], nums[i]
		else:
			i += 1
	oparr = []
	# After sorting the list enumerate to check if the index-1 pos matches
	for index,val in enumerate(nums):
		if (val-1) != index:
			oparr.append(val)
	return oparr

# Here one number is extra and one number is misising
# https://leetcode.com/problems/set-mismatch/submissions/
def findErrorNums(nums):
	i = 0
	while i < len(nums):
		correct = nums[i] - 1
		if nums[correct] != nums[i]:
			nums[i], nums[correct] = nums[correct], nums[i]
		else:
			i += 1

	oparr = []
	for index, val in enumerate(nums):
		if (val - 1) != index:
			oparr.append(val)
			oparr.append(index + 1)
	return oparr

# https://leetcode.com/problems/first-missing-positive/
def firstMissingPositive(nums):
	i = 0
	while i < len(nums):
		correct = nums[i] - 1
		if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]:
			nums[i], nums[correct] = nums[correct], nums[i]
		else:
			i += 1

	for index in range(len(nums)):
		if nums[index] != index + 1:
			return index + 1

	return len(nums) + 1

if __name__ == '__main__':
	print(cyclic_sort([1,2,2,4]))
	print(findDuplicates([4,3,2,7,8,2,3,1]))
	print(missingNumber([3,0,1]))
	print(findErrorNums([3,2,2]))
	print(firstMissingPositive([3,4,-1,1]))