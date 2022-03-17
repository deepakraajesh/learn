from collections import OrderedDict
n = int(input())
newdict = OrderedDict()
for i in range (n):
    item, space, amount = input().rpartition(' ')
    print (item, space, amount)
    newdict[item] = newdict.get(item,0) + int(amount)
    print(newdict)
print(*[" ".join([item, str(price)]) for item, price in newdict.items()], sep="\n")