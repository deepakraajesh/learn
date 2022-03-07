import re
lengt = 10
regex_patt = r"[A-Z|a-z|0-9]"
uid = input()
if (len(uid) == lengt and re.match(regex_patt,uid)):
    print("Valid")
else:
    print('Invalid')