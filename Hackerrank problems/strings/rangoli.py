import math
from turtle import width

ch = []
ini = 'a'
for i in range(0,26):
    if i == 0:
        ch.append(ini)
    else:
        ch.append(chr(ord(ini)+i))

sizenum = int(input())
height = sizenum + (sizenum-1)
widt = height + (height-1)
mid = math.ceil(height/2)

for i in range(1,mid+1):
    if (i==mid):
        print("None")