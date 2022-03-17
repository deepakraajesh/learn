S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)
'''
My Solution
import re
S = input()
k = input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',S):
    anymatch = 'Yes'
    temp = []
    temp.append(m.start(1))
    temp.append(m.end(1)-1)
    print (tuple(temp))
if anymatch == 'No':
    print (-1, -1)
    '''