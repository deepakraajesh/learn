sa=input()
sb=input()
res=""
for i in range(len(sa)):
    if (sa[i]==sb[i]):
        res+="0"
    else:
        res+="1"
print(res)