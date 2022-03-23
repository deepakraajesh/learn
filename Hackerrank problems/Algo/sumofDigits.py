def sumdig(n, k):
    if k == len(n) == 1:
        return int(n)
    res = 0
    for num in n:
        res += int(num)
    return sumdig(str(res*k),1)
if __name__=='__main__':
    nk=list(input().split())
    nk[0]=nk[0]*int(nk[1])
    print(sumdig(nk[0]))
#Still 3 test cases failed
'''
from collections import Counter
def sumdig (n):
    c=Counter(n)
    sum=0
    for key,value in c.items():
        sum+=int(key)*int(value)
    if (len(str(sum)))>1:
        sum=sumdig(str(sum))
    return sum
if __name__=='__main__':
    nk=list(input().split())
    nk[0]=nk[0]*int(nk[1])
    print(sumdig(nk[0]))
    '''
# This solution works but time limit exceeds
'''
def sumdig (n):
    sum=0
    for i in n:
        sum+=int(i)
    if(len(str(sum)))>1:
        sum=sumdig(str(sum))
    return sum
if __name__=='__main__':
    nk=list(input().split())
    nk[0]=nk[0]*int(nk[1])
    print(sumdig(nk[0]))
    '''