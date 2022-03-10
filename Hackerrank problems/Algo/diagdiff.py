n = int(input())
sq=[]
for i in range (n):
    l = list(map(int,input().split()))
    sq.append(l)
suml,sumr = 0,0
j=n-1
for i in range(n):
    suml += sq[i][i]
    sumr += sq[i][j]
    j-=1
print(abs(sumr-suml))