# Cycle Sort is a algorithm which you should use when they give you the term 1 - N
# Here all the elements are sorted in from 0,1,2 - N in ascending order
# Time complexity - O(N) but wont work if the order is changed

def cyclic_sort(nums):
	i = 0
	while i < len(nums):
		correct = nums[i]
		#correct = nums[i] - 1 ---> if zero is not included in the list
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



if __name__ == '__main__':
	print(cyclic_sort([0,2,1]))
	print(missingNumber([3,0,1]))