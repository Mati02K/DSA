# Two Pointers is one of the most popular techiques in solving algorithms
# Here we take two pointers point at some particular indices based on the problem and then traverse to find the solution.

#  Reverse Only Letters ---> In this problem we are tasked to reverse the string but only characters also in same position of the given string.
# In this approach we are going to take one pointer at beginning and one at the last and traverse from both the side and stopif we found out a non-string and append if it is from first pointer else just continue if it is from last pointer

def reverseOnlyLetters(s):
	op = ''
	i = 0
	j = len(s) - 1
	while i < len(s) and j >= 0:
		ch1 = s[i]
		ch2 = s[j]
		if ch2.isalpha() != True:
			j -= 1
			continue
		if ch1.isalpha():
			op += ch2
			j -= 1
		else:
			op += ch1
		i += 1
	while i < len(s):
		op += s[i]
		i += 1
	return op


# 3 Sum or closest to the 3 sum
def threeSum(arr, target):
	arr.sort()
	for index in range(len(arr) - 2):
		element = arr[index]
		currtarget = target - element
		start = index + 1
		end = len(arr) - 1
		currsum = 0
		while start < end:
			currsum = arr[start] + arr[end]
			# Currsum is less move left pointer else move right pointer
			if currsum == currtarget:
				return target
			elif currsum < currtarget:
				start += 1
			else:
				end -= 1

# Return the closest to the target
def threeSumClosest(arr,target):
	arr.sort()
	res = sum(arr[:3])

	for i in range(len(arr)-2):
		start = i + 1
		end = len(arr) - 1
		while start < end:
			currsum = arr[i] + arr[start] + arr[end]
			if abs(currsum - target) < abs(res - target):
				res = currsum
			if currsum < target:
				start += 1
			else:
				end -= 1
	return res

if __name__ == '__main__':
	print(reverseOnlyLetters("Qedo1ct-eeLg=ntse-T!"))
	# print(threeSumClosest([ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ],-1))
	print(threeSum([1,4,7,9,11], 12))
	print(threeSumClosest([0,1,2], 0))
	print(threeSumClosest([1,4,7,9,11], 10))


