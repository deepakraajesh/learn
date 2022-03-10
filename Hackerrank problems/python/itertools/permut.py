from itertools import permutations
inp = input().split()
res = sorted(list(permutations(inp[0],int(inp[1]))))
for i in res:
    if (inp[1]=='1'):
        print(((str(i).replace("',)","")).replace("('","")))
    else:
        print(((str(i).replace("', '","")).replace("('","")).replace("')",""))