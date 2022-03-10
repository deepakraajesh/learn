cube = lambda x: x*x*x

def fibonacci(n):
    if (n==0 or n==1):
        return [0]
    fir, sec = 0,1
    ans = [0,1]
    for i in range (n-2):
        res = fir + sec
        ans.append(res)
        fir,sec = sec,res
    return ans

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))