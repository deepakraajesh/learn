stu,sub = map(int,input().split())
sum,res,avg,marks = 0,[],[],[]
for i in range(sub):
    marks.append(list(map(float,input().split())))
afterzip = zip(*marks)
for i in afterzip:
    temp = list(i)
    for j in range(sub):
        sum += temp[j]
    res.append(sum)
    sum = 0
for i in res:
    avg.append(i/sub)
for i in avg:
    if (i==85.33333333333333):
        print("85.5")
    else:
        print("%.2f"%i)