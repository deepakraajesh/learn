import numpy

xyz = tuple(map(int,input().split()))
print(xyz)
print (numpy.zeros(xyz, dtype = numpy.int))
print (numpy.ones(xyz, dtype = numpy.int))