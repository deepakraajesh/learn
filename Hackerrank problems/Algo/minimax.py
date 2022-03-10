from numpy import append


def miniMaxSum(arr):
    print(sum(arr)-max(arr),end=" ")
    print(sum(arr)-min(arr))
    #sum of array provides entire sum, reducing minimum number provides maximum sum of 4 elements, reducing maximum number provides minimum sum of 4 elements

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)