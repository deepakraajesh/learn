import numpy
nmp = list(map(int,input().split()))
arrA,arrB = [],[]
for i in range (nmp[0]):
    arrA.append(list(map(int,input().split())))
for i in range (nmp[1]):
    arrB.append(list(map(int,input().split())))
arrA= numpy.array(arrA)
arrB=numpy.array(arrB)
print (numpy.concatenate((arrA,arrB),axis=1))