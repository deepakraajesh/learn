class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (low % 2 == 0 and high % 2 ==0):
            return int((high-low)/2)
	
        else:
            return int(((high-low)/2)+1)
s=Solution()
low,high=int(input()),int(input())
print(s.countOdds(low,high))