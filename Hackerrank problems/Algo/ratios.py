def plusMinus(arr):
    pos,neg,zer = 0,0,0
    for i in arr:
        if i<0:
            neg += 1
        elif i==0:
            zer += 1
        elif i>0:
            pos += 1
    print("{:.6f}".format(pos/len(arr)))
    print("{:.6f}".format(neg/len(arr)))
    print("{:.6f}".format(zer/len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)