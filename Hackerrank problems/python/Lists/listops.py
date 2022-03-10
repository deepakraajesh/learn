from collections import Counter
dummy = input()
listA = sorted(list(map(int,input().split())))
c = Counter(listA)
print(c)
res = [k for k,v in c.items() if v==1]
#[ return_value/executable command  for (i or key,value (for dictionaries etc..)) in range/list/dict condition]
for i in res:
    print(i)