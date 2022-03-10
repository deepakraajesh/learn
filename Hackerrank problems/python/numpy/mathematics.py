import numpy
nm = list(map(int,input().split()))
a,b=[],[]
for i in range(nm[0]):
    tempa = list(map(int,input().split()))
    a.append(tempa)
for i in range(nm[0]):
    tempb = list(map(int,input().split()))
    b.append(tempb)
a=numpy.array(a)
b=numpy.array(b)
print (a+b)
print (a-b)
print (a*b)
print (a//b)
print (a%b)
print (a**b)