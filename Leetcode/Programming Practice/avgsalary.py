class Solution:
    def average(self, salary) -> float:
        sum=0
        salary.sort()
        salary=salary[1:-1]
        for i in salary:
            sum += i
        return float(sum/len(salary))

s=Solution()
sal=list(map(int,input().split()))
s.average(sal)