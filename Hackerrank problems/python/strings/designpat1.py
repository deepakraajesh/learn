import math

s = input().split()
n = int(s[0])
m = int(s[1])
mid = math.ceil(n/2)
des = ".|."

for i in range (1,mid+1):
    if (i==mid):
        print("WELCOME".center(m,"-"))
    elif (i<mid):
        ndes = des * (i+(i-1))
        print(ndes.center(m,"-"))

for i in range (mid-1,0,-1):
    mdes = des * (i+(i-1))
    print(mdes.center(m,"-"))