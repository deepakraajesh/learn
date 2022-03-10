import re

regex_patt = r"([0-9])\1{2,}"
tup = re.match(regex_patt,input())
print(tup.groups(0))
'''if (len(tup.groups)!=0):
    print(tup[0])
else:
    print("-1")
    '''
