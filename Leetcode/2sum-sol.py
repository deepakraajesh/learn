nums = [1,2,4,3]
target = 6
class Solution:
    def twoSum(self, nums, target):
        for i,j in enumerate(nums):
            if target - j in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - j) + (i + 1)]