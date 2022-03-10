import numpy

def arrays(arr):
    arr.reverse()
    narr = numpy.array(arr,float)
    return narr

arr = list(map(int,input().split()))
result = arrays(arr)
print(result)