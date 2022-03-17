from itertools import product
K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
#We have to provide the cartesion product of arrays
'''My Program
n,m = map(int,input().split())
s,res,sq,sum=[],[],[],0
for i in range(n):
    s.append(list(map(int,input().strip().split(' ')[1:])))
for i in s:
    res.append(max(i))
    print(max(i))
for i in res:
    sq.append(i*i)
    print(i*i)
for i in sq:
    sum+=i
print(sum)
print(sum%m)
'''
