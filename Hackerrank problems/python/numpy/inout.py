import numpy
a,b=[],[]
a.append(list(map(int,input().split())))
b.append(list(map(int,input().split())))
ar = numpy.array(a)
br = numpy.array(b)
print (numpy.inner(ar,br)[0][0])
print (numpy.outer(ar,br))