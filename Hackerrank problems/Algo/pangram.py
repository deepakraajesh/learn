import string
s=input()
s=set(s.lower())
try:
    s.remove(' ')
    a=set(string.ascii_lowercase)
    for i in s:
        a.discard(i)
    if len(a)>0:
        print("not pangram")
    else:
        print("pangram")
except:
    a=set(string.ascii_lowercase)
    for i in s:
        a.discard(i)
    if len(a)>0:
        print("not pangram")
    else:
        print("pangram")