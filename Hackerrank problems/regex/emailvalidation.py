import email.utils
import re

n=int(input())
for i in range(n):
    em = input()
    paremail = email.utils.parseaddr(em)
    if (re.match(r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$",paremail[1].lower())):
        print(email.utils.formataddr(paremail))
#formemail = email.utils.formataddr(paremail)