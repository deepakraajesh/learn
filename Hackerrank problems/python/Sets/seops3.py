dummy = input()
main = set(map(int,input().split()))
nocomm = int(input())

for i in range(0,nocomm):
    temp=input().split()
    if (temp[0]=="intersection_update"):
        insset = set(map(int,input().split()))
        main.intersection_update(insset)
    elif (temp[0]=="symmetric_difference_update"):
        symdifset = set(map(int,input().split()))
        main.symmetric_difference_update(symdifset)
    elif (temp[0]=="difference_update"):
        difset = set(map(int,input().split()))
        main.difference_update(difset)
    elif (temp[0]=="update"):
        upd = set(map(int,input().split()))
        main.update(upd)
sum = 0
for i in main:
    sum += i
print (sum)