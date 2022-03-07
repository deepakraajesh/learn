from collections import namedtuple
from unicodedata import name
num = int(input())
ptr = namedtuple('Point','id marks name class')
resl = []
for i in range(num):
    temp = ptr(input().split())
    resl.append()