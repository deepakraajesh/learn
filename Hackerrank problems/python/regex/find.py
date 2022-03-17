import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))

'''
My Solution.
import re
s = input()
m=re.findall('[AEIOUaeiou]{2,}',s)
for i in m:
    print (i)
    '''