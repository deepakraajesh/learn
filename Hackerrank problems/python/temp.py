import re
n = int(input())
for i in range(n):
    hexa = input()
    res = re.search(r"^#[0-9|A-F|a-f]{3,6}",hexa)
    for i in res:
        print(i)