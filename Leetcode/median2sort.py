class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num3 = sorted(nums1+nums2)
        mid=len(num3)//2
        if (len(num3)%2==0):
            res=(num3[mid]+num3[mid-1])/2
        else:
            res=num3[mid]
        print("{:.6f}".format(res))

if __name__=='__main__':
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    s=Solution()
    s.findMedianSortedArrays(nums1,nums2)