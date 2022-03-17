import string
lAlp = string.ascii_lowercase
uAlp = string.ascii_uppercase
dummy = int(input())
s = input()
k=int(input())
k=k%26
res=''
nlAlp = lAlp[k:26]+lAlp[0:k]
nuAlp = uAlp[k:26]+uAlp[0:k]
mapAlp = {}
for i in range(26):
    mapAlp[lAlp[i]]=nlAlp[i]
    mapAlp[uAlp[i]]=nuAlp[i]
for i in s:
    if (i in mapAlp):
        res+=mapAlp.get(i)
    else:
        res+=i
print(res)