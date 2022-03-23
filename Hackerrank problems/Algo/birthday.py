from collections import Counter

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
c=Counter(candles)
print(c.get(max(c,key=c.get)))