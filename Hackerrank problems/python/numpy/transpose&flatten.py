import numpy

nm = list(map(int,input().split()))
array = numpy.array([input().strip().split() for _ in range(nm[0])], int)
#print (array)
print (array.transpose())
print (array.flatten())