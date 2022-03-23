m=((10**9)+7)
n=input()
ar = list(map(int,input().split()))
ans=1
for i in ar:
    ans=(ans*i)%m
print(ans)