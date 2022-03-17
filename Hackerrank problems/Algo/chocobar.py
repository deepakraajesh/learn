dummy=input()
s = list(map(int,input().split()))
d,m = map(int,input().split())
sum,i = 0,0
res = []
sumres = []
for i in range(len(s)-(m-1)):
    res.append(s[i:i+m])
#print(res)
for i in range(len(res)):
    for j in range(m):
        sum += res[i][j]
    sumres.append(sum)
    sum=0
#print(sumres)
count=0
for i in range(len(sumres)):
    if sumres[i] == d:
        count+=1
print(count)