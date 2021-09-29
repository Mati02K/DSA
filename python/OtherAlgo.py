# This files contains other important algorithms

# To find Unit Digit of a number

def findunitdigit(num):
    unitno = num % 10
    return unitno
    
# number of digits in a number

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

#Program to cocatenate two numbers
def numConcat(num1, num2):
  
     # find number of digits in num2
     digits = len(str(num2))
  
     # add zeroes to the end of num1
     num1 = num1 * (10**digits)
  
     # add num2 to num1
     num1 += num2
  
     return num1

# Find the first digit
def firstDigit(n) :
 
    # Remove last digit from number
    # till only one digit is left
    while n >= 10:
        n = n / 10;
     
    # return the first digit
    return int(n)

# Palindrome of two numbers
def isPalindrome(x):
    if x < 0 or x % 10 ==x:
        return False
        
    temp = x
    revnum = 0
    
    while x > 0:
        revnum = revnum * 10 + x % 10
        x = x // 10

    return revnum == temp

# Fibonacci Best Approach
def fibonacci(n):
	a = 0
	b = 1

	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")

	# Check is n is equal
	# to 0
	elif n == 0:
		return 0

	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

# Pascal's Traingle
# Read More info abput pascals traingle here https://en.wikipedia.org/wiki/Pascal%27s_triangle
def pascaltraingle(numRows):
	triangle = []
	if numRows == 0:
		return triangle

	first_row = [1]
	triangle.append(first_row)

	for i in range(1, numRows):
		prevrow = triangle[i - 1]
		row = []
		row.append(1)
		j = 1
		while j < i:
			value = prevrow[j - 1] + prevrow[j]
			row.append(value)
			j += 1
		row.append(1)
		triangle.append(row)

	return triangle

# Pascal Traingle is the position where start and end elements are 1 and in between elements are sum of upper two arrays
def pascaltriangle(rowIndex):
	pascal = [[1] * i for i in range(1, rowIndex + 2)]
	if rowIndex < 2:
		return pascal[rowIndex]
	for i in range(2, len(pascal)):
		for j in range(1, len(pascal[i]) - 1):
			formula = pascal[i - 1][j - 1] + pascal[i - 1][j]
			pascal[i][j] = formula

	return pascal


if __name__ == '__main__':
    print(findunitdigit(5692))
    print(countDigit(569))
    print(numConcat(906, 91))
    print(firstDigit(569))
    print(isPalindrome(1122))
    print(pascaltraingle(5))
