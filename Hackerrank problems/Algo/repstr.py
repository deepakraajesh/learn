from collections import Counter
s=input()
n=int(input())
mul = (n//len(s))+1
s=s*mul
s=s[0:n]
c=Counter(s)
print(c.get(max(c,key=c.get)))