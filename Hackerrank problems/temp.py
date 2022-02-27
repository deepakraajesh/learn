import re
main = input()
sstr = input()
res = []
m = re.search(sstr,main)
l = [m.start(),m.end()]
res.append(l)
print (res)