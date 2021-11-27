# This file consits some of the very important string related problems

#  Find the subsequence of a character in a string
# https://www.youtube.com/watch?v=4jY57Ehc14Y
# We will be using KMP Algorithm


def findSequnce(txt,pattern):
	if pattern == "":
		return 0
	lps = [0] * len(pattern)  # Latent Prefix suffix
	prevLps, i = 0, 1

	while i < len(pattern):
		if pattern[i] == pattern[prevLps]:
			lps[i] = prevLps + 1
			prevLps += 1
			i += 1
		elif prevLps == 0:
			lps[i] = 0
			i += 1
		else:
			prevLps = lps[prevLps - 1]

	print(lps)
	i = 0 # pointer for text
	j = 0 # pointer for pattern

	while i < len(txt):
		if txt[i] == pattern[j]:
			i, j = i + 1, j + 1
		else:
			if j == 0:
				i += 1
			else:
				j = lps[j - 1]
		if j == len(pattern):
			return i - len(pattern)

	return -1

if __name__ == '__main__':
	print(findSequnce("aaabcdeaaabcddeaaabcdrfaabcdmb","aabcdmb"))