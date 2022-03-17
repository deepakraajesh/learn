n=int(input())
for i in range(n):
    j = int(input())
    j="{:032b}".format(j)
    j=str(j)
    res=[]
    for i in j:
        if (i=="1"):
            res.append(0)
        else:
            res.append(1)
listToStr = ''.join([str(elem) for elem in res])
print(int(listToStr,2))