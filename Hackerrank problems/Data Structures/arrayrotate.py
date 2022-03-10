n,d = (int(x) for x in input().split())
l = [int(x) for x in input().split()]
length = len(l)
new = [0 for i in range(len(l))]
for i in range(length):
    #Using Maths
    o = i-d
    new[o]=str(l[i])
print(" ".join(new))

'''
My solution without using collections
_________________________________________
inp = list(map(int,input().split()))
iniarray = list(map(int,input().split()))
currrot = 0
while (inp[1]>currrot):
    iniarray.insert(inp[0],iniarray[0])
    iniarray = iniarray[1:]
    currrot += 1
    print (iniarray)
    '''