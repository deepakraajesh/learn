n=int(input())
a,res=[],[]
c=0
for i in range(n):
    a.append(input())
for i in range(len(a)):
    for j in a[i]:
        if (j!='0' and int(a[i])%int(j)==0):
            c+=1
    print(c)
    c=0