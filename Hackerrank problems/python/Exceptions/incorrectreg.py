import re
n = int(input())
for i in range(n):
    reg = input()
    sol = "True"
    try:
        re.compile(reg)
    except:
        sol = "False"
    print (sol)