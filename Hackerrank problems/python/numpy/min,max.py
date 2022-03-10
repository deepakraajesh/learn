import numpy
row,col = map(int,input().split())
inparr = []
for i in range (row):
    inparr.append(list(map(int,input().split())))
res = numpy.array(inparr)
minim = numpy.min(res,axis=1)
print(numpy.max(minim))