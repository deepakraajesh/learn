from itertools import combinations_with_replacement
let, n = map(str,input().split())
n=int(n)
res=[]
for j in combinations_with_replacement(sorted(let), n):
    print(''.join(j))