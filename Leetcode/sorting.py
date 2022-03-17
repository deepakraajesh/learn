class Solution(object):    
    def removeDuplicates(self, nums):
        num = sorted(list(set(nums)))
        res,s=[],'['
        for i in range(len(num)):
            res.append(num[i])
        for i in range(len(nums)-len(num)):
            res.append('_')
        for i in res:
            s+=str(i)+","
        s+="\b]"
        print(s)

s=Solution()
nums=input()
nums=nums[1:-1]
nums=list(map(int,nums.split(',')))
res = s.removeDuplicates(nums)