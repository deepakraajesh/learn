from collections import Counter
l = [1, 2, 3, 4, 3, 2, 1]
count = Counter(l)
for letter, valu in count.items():
    if (valu == 1):
        print(letter)

'''
This is how the counter itself works:
>>> word = "mississippi"
>>> counter = {}

>>> for letter in word:
...     if letter not in counter:
...         counter[letter] = 0
...     counter[letter] += 1
...

>>> counter
{'m': 1, 'i': 4, 's': 4, 'p': 2}
'''