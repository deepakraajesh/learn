if __name__ == "__main__":
    n = int(input())
    a=[]
    b=[]
    i=0
    for i in range(0,n):
        temp1=int(input())
        a.append(temp1)
        temp2=int(input())
        b.append(temp2)

    for i in range(0,n):
        try:
            if(a[i]%b[i]==0):
                c=a[i]//b[i]
                print(c)
            i+=1
        except ValueError as err:
            print(err)
            i+=1
                