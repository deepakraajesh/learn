import re
n = int(input())
for i in range (n):
    # [+/-][0-9].{1[0-9]}
    print(bool(re.match("^[-+]?[0-9]*\.[0-9]+$",input())))