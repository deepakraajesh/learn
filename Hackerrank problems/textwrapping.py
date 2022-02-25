import textwrap

st = input()
widt = int(input())
wrappe = textwrap.TextWrapper(width=widt)
stri = wrappe.fill(text=st)
print(stri)