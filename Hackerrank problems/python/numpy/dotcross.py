import numpy
n = int(input())
a,b = [],[]
for i in range (n):
    a.append(list(map(int,input().split())))
for i in range (n):
    b.append(list(map(int,input().split())))   
arra = numpy.array(a)
arrb = numpy.array(b)
print (numpy.dot(a,b))
print (numpy.cross(a,b))