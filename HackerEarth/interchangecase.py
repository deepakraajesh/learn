s=input()
res=''
for i in s:
    if (i.isupper()):
        res+=str.lower(i)
    else:
        res+=str.upper(i)
print(res)