def check(li):
    flr = float("inf")
    left_run = 0
    right_run = len(li)-1
    left_val = li[0]
    right_val = li[right_run]
    res = []
    while (left_run>=right_run):
        if left_val>=right_val and left_val<=flr:
            res.append(left_val)
            flr = left_val
            left_run += 1
        elif right_val>left_val and right_val<=flr:
            res.append(right_val)
            flr = right_val
            right_run -=1
        else:
            return "No"
    return "Yes"

n = int(input())
for i in range(n):
    siz = int(input())
    for j in range(siz):
        l = list(map(int,input().split()))
        print(check(l))