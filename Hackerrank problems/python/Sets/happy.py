#Working in Hackerrank
n,m = input().split()
count = 0
array = input().split()
set_a,set_b = set(input().split()),set(input().split())
for i in array:
    if i in set_a and i not in set_b:
        count += 1
    if i in set_b and i not in set_a:
        count -= 1
print(count)

'''
My Approach
dummy = input()
setM = set(map(int,input().split()))
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))
print(sum([(i in setA)-(i in setB) for i in setM]))
'''
'''
Another approach
dummy = input()
setM = set(map(int,input().split()))
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))
happypl = setA.intersection(setM)
happymi = setB.intersection(setM)
print(len(happypl)-len(happymi))
'''