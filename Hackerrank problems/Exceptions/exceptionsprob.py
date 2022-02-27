if __name__ == "__main__":
    n = int(input())
    res = []
    for i in range(0,n):
        try:
            a,b = map(int,input().split())
            res.append(a//b)
        except Exception as e:
            temp2 = "Error code: " + str(e)
            res.append(temp2)
    for i in res:
        print(i)