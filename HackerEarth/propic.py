size=int(input())
n=int(input())
for i in range(n):
    s=list(map(int,input().split()))
    if (s[0]==size and s[1]==size):
        print("ACCEPTED")
    elif(s[0]>size and s[1]>size):
        print("CROP IT")
    else:
        print("UPLOAD ANOTHER")