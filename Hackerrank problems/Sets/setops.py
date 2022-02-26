if __name__ == "__main__":
    m = int(input())
    st = set(map(int,input().split()))
    n = int(input())
    ts = set(map(int,input().split()))

    differ = st.symmetric_difference(ts)
    for i in differ:
        print (i)