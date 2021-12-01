'''
#
# # This is a playground file check, test , run and play around with your code here...
'''

from collections import deque

'''
#
# # This is a playground file check, test , run and play around with your code here...
'''

from collections import deque


def maxProduct(nums):
    res = nums[0]
    curMax, curMin = 1, 1

    for num in nums:
        tmp = curMax * num
        curMax = max(tmp, curMin * num, num)
        curMin = min(tmp, curMin * num, num)
        res = max(res, curMax)

    return res

if __name__ == '__main__':
    key = [2,-5,-2,-4,3]
    print(maxProduct(key))