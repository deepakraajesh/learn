import numpy
row,col = map(int,input().split())
inparr = []
for i in range (row):
    inparr.append(list(map(int,input().split())))
res = numpy.array(inparr)
print(numpy.mean(res,axis=1))
print(numpy.var(res,axis=0))
print(round(numpy.std(res),11))