import re
no = int(input())
res = []
for i in range(0,no):
    temp = input()
    if (re.match("^9.{9}" or "^8.{9}" or "^7.{9}",temp)):
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)