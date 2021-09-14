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


if __name__ == '__main__':
	print(reverseOnlyLetters("Qedo1ct-eeLg=ntse-T!"))


