from itertools import combinations
let, n = map(str,input().split())
n=int(n)
res=[]
for i in range(1, n+1):
    for j in combinations(sorted(let), i):
        print(''.join(j))