import math
'''
Bit Manipulation
Some Basics of Bit Manipulation
 & --- > return 1 when both are 1
 or || ----> return 1 when either is one
 ^ ---> returns 1 when exactly either is one, but not both (0,1 or 1,0)
 (Left Shift) a << b ---> adds b no of zeros to right
 a << b = a * 2^b
(Right Shift) a >> b ----> removes b times digits from the left
 a >> b = a / 2^b
 a & 1 ---> return LSB (Least Significant Bit) or last bit
'''

# Finding a number is odd or even using bitmanipulation
def oddoreven(n):
	if n == 0:
		return "NEUTRAL"
	# As per the 8 4 2 1 code if in the 1 place there is a one the number is odd else zero
	# n & 1 retruns the last binary number(i.e 1 place number in 8 4 2 1 code)
	# Return true if odd else even
	# Last digit is known as LSB(Least Significant Bit)
	return "ODD" if (n & 1) == 1 else "EVEN"

# Find the unique number in the array
def findUnique(elements):
	unique = 0
	for element in elements:
		# 2 ^ 3 ^ 3 ^ 4 ^ 2 ^ 6 ^ 4 = (2^2) ^ (3^3) ^ (4^4) ^ (6^0) = 6
		unique ^= element
	return unique

# Magic number is the total binary representations of a number risen to the power of 5
# https://www.geeksforgeeks.org/find-nth-magic-number/
def magicno(n):
	ans = 0
	if n == 0:
		return ans
	base = 5
	while n > 0:
		last = n & 1
		ans += last * base
		n = n >> 1  # Right shif so that we can get the next binary no
		base = base * 5 # Keep increasing the power of 5 upto len of binary no

	return ans

# No of Binary Digits in a given base -- for ex 10 in base 2 = 1010 ( so total 4)
def totalndigit(base,number):
	ans = int((math.log(number) / math.log(base))) + 1 # --> Formula
	# ans = int(math.log(10,2)) + 1 ---> Another solution
	return ans

def poweroftwo(n):
	if n == 0:
		return False
	return n & (n-1) == 0 # Take any example and see

# Find the no of set bits in a number for ex: n = 9 (1001) --> only 2 ones are present so answer 2
def findsetbits(n):
	count = 0
	# while n > 0:   # --- Time complexity (O(n))
	# 	if n & 1 == 1:
	# 		count +=1
	# 	n = n >> 1
	while n > 0: # ----> Time Complexity ((O(logn))
		count +=1
		n = n & (n-1)
	return count

# XOR Range -> Write a Function a to return xorrange from 0 to a (There is a pattern followed)
def xorRange(a):
	if a % 4 == 0:
		return a
	if a % 4 == 1:
		return 1
	if a % 4 == 2:
		return a + 1
	return 0

# Reverse Bits of a given number. For ex Input -> 8 -> 00000000000000000000000000001000 output --->    268435456 (00010000000000000000000000000000)
def reverseBits(n):
	res = 0
	# Bcoz 32 bits is the max
	for i in range(32):
		bit = (n >> i) & 1
		res = res | (bit << (31 - i))

	return res

# Hamming Distance Problem , First XOR the the inputs and find the no of set bits(1) in the result
def hammingDistance(x, y):
	res = x ^ y
	count = 0
	for _ in range(32):
		curr = res & 1
		if curr == 1:
			count += 1
		res = res >> 1

	return count

if __name__ == '__main__':
	print(oddoreven(21))
	print(findUnique([2,3,3,4,2,6,4]))
	print(magicno(6))
	print(totalndigit(2,10))
	print(poweroftwo(32))
	print(findsetbits(7))
	print(xorRange(9) ^ xorRange(2)) # ---> this is the XOR Range from 3 to 9
	print(reverseBits(8))
	print(hammingDistance(1,4))