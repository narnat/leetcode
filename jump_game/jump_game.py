#!/usr/bin/env python3

class Solution:
    def canJump(self, nums):
        if not nums:
            return False
        l = len(nums)
        steps = nums[0]
        # print("***********")
        i = 0
        while True:
            if steps <= 0 and i < l - 1:
                return False
            if i >= l - 1:
                return True
            # print(steps, i)
            steps -= 1
            i += 1
            steps = max(steps, nums[i])
            # print("After", steps, i)
if __name__ == '__main__':
    canJump = Solution().canJump
    assert(canJump([2,3,1,1,4]) == True)
    assert(canJump([3,2,1,0,4]) == False)

    print("All good!!!")
