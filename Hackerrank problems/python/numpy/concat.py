import numpy

nmp = list(map(int,input().split()))
for i in range (nmp[0]):
    arrA = numpy.array([input().split(),int])
for i in range (nmp[1]):
    arrB = numpy.array([input().split(),int])
print(numpy.concatenate(arrA,arrB),axis=0)