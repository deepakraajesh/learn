if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    noc = int(input())
    for i in range(0,noc):
        temp = input().split()
        if temp[0]=="pop":
            s.pop()
        elif temp[0]=="remove":
            s.remove(int(temp[1]))
        elif temp[0]=="discard":
            s.discard(int(temp[1]))
    sum = 0
    for i in s:
        sum += i
    print(sum)