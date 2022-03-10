if __name__ == '__main__':
    s = []
    N = int(input())
    for i in range(0,N):
        getinp=input().split()
        if (getinp[0]=="append"):
            s.append(int(getinp[1]))
        elif (getinp[0] == "insert"):
            s.insert(int(getinp[1]),int(getinp[2]))
        elif (getinp[0] == "remove"):
            s.remove(int(getinp[1]))
        elif (getinp[0] == "pop"):
            s.pop(int(getinp[1]))
        elif (getinp[0] == "reverse"):
            s.reverse()
        elif (getinp[0] == "sort"):
            s.sort()
        elif (getinp[0] == "print"):
            print(s)