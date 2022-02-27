from itertools import combinations

from numpy import sort
inp = input().split()
res = list(combinations(inp[0],int(inp[1])))
nres = []
mres = []
for i in inp[0]:
    nres.append(i)
for i in res:
    if inp[1]=='1':
        mres.append((str(i).replace("('","")).replace("',)",""))
    else:
        mres.append(((str(i).replace("('","")).replace("')","")).replace("', '",""))
res = []
res = sorted(mres)
ores = sorted(nres)
for i in ores:
    print(i)
for i in res:
    print(i)