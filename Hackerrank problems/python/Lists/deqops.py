import collections

n = int(input())
q = collections.deque([])
for i in range(0,n):
    s = input().split()
    if (s[0]=="append"):
        q.append(int(s[1]))

    elif (s[0]=="appendleft"):
        q.appendleft(int(s[1]))
    
    elif (s[0]=="extend"):
        q.extend(int(s[1]))

    elif (s[0]=="extendleft"):
        q.extendleft(int(s[1]))

    elif (s[0]=="popleft"):
        q.popleft()

    elif (s[0]=="pop"):
        q.pop()

    elif (s[0]=="remove"):
        q.remove(int(s[1]))

    elif (s[0]=="rotate"):
        q.rotate(int(s[1]))

print (*q, sep=" ")