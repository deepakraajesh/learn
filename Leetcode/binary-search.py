class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        mid = 0
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                print(mid)
                return mid
        print(-1)
        return -1

s=Solution()
s.search([-1,0,3,5,7,9,12],9)