def missingNumbers(arr, brr):
    for i in arr:
        if i in brr:
            brr.remove(i)
    return set(sorted(brr))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    print(missingNumbers(arr, brr))