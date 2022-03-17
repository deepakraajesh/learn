from collections import Counter
n = int(input())
s = []
for i in range(n):
    s.append(input())
res = Counter(s)
print(len(res))
for i,j in res.items():
    print(j, end=' ')