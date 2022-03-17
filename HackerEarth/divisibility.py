N = int(input())
data = [int(x) for x in input().split()]
s=''
for i in data:
    s+=str(i%10)
if(int(s)%10==0):
    print("yes")
else:
    print("No")