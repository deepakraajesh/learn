from collections import deque

class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums)-1
        res = deque()
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res.appendleft(nums[right]**2)
                right -= 1
            else:
                res.appendleft(nums[left]**2)
                left += 1
        return res

s=Solution()
s.sortedSquares([-2,-3,0,1,5])