arr=[]
for i in range (7):
    arr.append(int(input()))
arr.sort()
mid = len(arr)//2
print(arr[mid])