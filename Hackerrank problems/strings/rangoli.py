import string
alpha = string.ascii_lowercase

n = int(input())
res = []
for i in range(n):
    s = "-".join(alpha[i:n])
    res.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(res[:0:-1]+res))

'''
4n - 3 is solved like this
height = n+(n-1) = 2n-1
Ex: if n = 3 => 2*3 -1 = 5 is the height
width = h+(h-1) = 2h-1
Ex: if n=3 => 2*5 -1 = 9 is the width
2h-1 => 2(2n-1)-1 => 4n-2-1 => 4n-3

res[:0:-1]
prints the list in reverse order excludes the first element (In this case the whole list except mid element. This is to print other half)
'''