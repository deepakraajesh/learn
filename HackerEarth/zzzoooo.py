from collections import Counter
s=input()
c = Counter(s)
if(c.get('z')*2==c.get('o')):
    print("Yes")
else:
    print("No")
#Use case is 1 'z' should have 2 'o' - zoo, zzoooo, zzzoooooo and so on
'''
import re
s=input()
reg=re.match("^z+o{2,}",s)
if(reg):
    print("yes")
else:
    print("No")
'''