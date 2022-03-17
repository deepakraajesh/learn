from collections import Counter
def lonelyint(ar):
    c =Counter(ar)
    for i in c:
        if (c.get(i)==1):
            print(i)

if (__name__=="__main__"):
    n = int(input())
    ar = list(map(int,input().split()))
    lonelyint(ar)