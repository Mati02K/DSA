#Recursion
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

def fact(n):
    if n == 0 or n==1:
        return 1
    # n * n-1 * n-2 (5 *4 * 3 ...)
    return n * fact(n-1)
def lengthOfLongestSubstring(s):
        # output = ''
        # temp = 0
        # prev = 0
        # for i in range(len(s)):
        #     if temp<len(s)-1:
        #         temp = i + 1
        #     if i > 0:
        #         prev = i - 1
        #     if (s[i] != s[temp] or i == temp) and s[i] not in output:
        #         if output == '':
        #             output = output + s[i]
        #         elif s[prev] in output:
        #              output = output + s[i]
        #         else:
        #             output = ''
        #             output = output + s[i]

        # lengthoutput = len(output)
        # if lengthoutput > 0:
        #     return lengthoutput
        # else:
        #     return 1
        n = 0
        b = []
        for i in s:
            if i not in b:
                b.append(i)
                if len(b) > n:
                    n = len(b)                
            else:
                b = b[b.index(i)+1:]
                b.append(i)
        return n
def reverse(x):
    newno = 0
    no = abs(x)
    i = 0
    while no > 0:
        digit = 10
        newno = (newno * digit) + no % 10
        no = no // 10
        
    if (newno > 2**31 -1) or (-newno < -2**31):
        return(0)
    if x >= 0:
        return newno
    else:
        return -newno
        
if __name__ == '__main__':
    print(fib(6))
    print(fact(5))
    print('M' in 'Mathesh')
    print(lengthOfLongestSubstring("pwwkew"))
    print(reverse(123))