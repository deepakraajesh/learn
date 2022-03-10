dummy = input()
shoeavail = list(map(int,input().split()))
nofcus = int(input())
amount = 0
for i in range(0,nofcus):
    temp = list(map(int,input().split()))
    if (temp[0] in shoeavail):
        amount += temp[1]
        shoeavail.remove(temp[0])
print(amount)