# This File contains a series of problems that deal with sliding window algorithm
# Sliding Window algorithm is moving the window or section of a problem with aim of solution and if a better solutions is found we replace it

#  Longest Substring without repeating characters
# We have to return a longest character sequence from the string where there is no repetition of each words
# For more info watch this video: https://www.youtube.com/watch?v=4i6-9IzQHwo
def lengthoflargestsubstring(string):
	if string == None or len(string) == 0:
		return 0
	# Initializing a set where if we see wheather we have seen a variable or not
	seen = set()
	#  We have three pointers i,j,max
	i = j = maximium = 0
	# i is the index where we visit the node and j is the position where we started if we face a situation of repeating characters and max = (i-j) + 1 to return the indexes moved
	while i < len(string):
		c = string[i]
		while c in seen:
			seen.remove(string[j])
			j+=1

		seen.add(c)
		maximium = max(maximium,(i-j)+1)
		i+=1

	return maximium

if __name__ == '__main__':
	print(lengthoflargestsubstring('MATHESH'))


