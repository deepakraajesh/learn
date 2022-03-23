def getMoneySpent(keyboards, drives, b):
    sum,temp=-1,0
    for i in keyboards:
        for j in drives:
            temp=i+j
            if (temp<=b and sum<temp):
                sum=temp
    return sum

if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)