import re
no = int(input())
for i in range(0,no):
    temp = input()
    if (re.match("^[7-9]\d{9}$",temp)):
        print("YES")
    else:
        print("NO")