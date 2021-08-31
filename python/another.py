# A complete working Python3 program to
# demonstrate deletion in singly
# linked list with class

class Solution:
    def removeDuplicates(self, nums):
        # prev = -1
        # lenlist = len(nums)-1
        # i = 0
        # while(i < lenlist):
        #     if nums[i] == prev:
        #         nums.remove(nums[i])
        #     prev = nums[i]
        #     lenlist = len(nums)-1
        #     if i > lenlist:
        #         i = 0
        #     else:
        #         i+=1

        # return len(nums)
        if len(nums) < 2:
            return len(nums)
        ulen = 0
        unique = None
        for i in range(len(nums)):
            if nums[i] != unique:
                unique = nums[i]
                nums[i] = None
                nums[ulen] = unique
                ulen += 1
            else:
                nums[i] = None
        return ulen


if __name__ == '__main__':
    # Driver program
    mylist = [0,0,1,1,1,2,2,3,3,4]
    # mylist = [0, 0, 1, 1, 1, 2]
    perm = Solution()
    print(perm.removeDuplicates(mylist))