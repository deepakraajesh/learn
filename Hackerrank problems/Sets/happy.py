dummy = input()
setM = set(map(int,input().split()))
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))

happy = 0

for i in setM:
    if (i in setA):
        happy += 1
    if (i in setB):
        happy -= 1
print(happy)
