class Solution(object):    
    def removeDuplicates(self, nums,v):
        res=[]
        for i in nums:
            if (i!=v):
                res.append(i)
            print(res)
s=Solution()
nums=list(map(int,input().split()))
v=int(input())
s.removeDuplicates(nums,v)
#Working solution
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                #you are changing the list itself
                nums[i] = x
                i += 1
        #You are returning number of elements in list which prints the modified list
        return i
"""