def isBadVersion(version):
    if version>3:
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1)==True:
            return 1
        
        start = 1
        end = n
		# as we know there will be a bad version, use while True which is faster than while start<=end.
        while True: 
            mid = start+(end-start)//2 # this is also faster than mid = (start+end)//2
            if isBadVersion(mid)==False:
                start = mid + 1
            elif isBadVersion(mid-1)==False:
                print (mid)
                return mid
            else:
                end = mid - 1

isBadVersion(3)
s=Solution()
s.firstBadVersion(7)