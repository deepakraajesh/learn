if __name__ == "__main__":
    m = int(input())
    st = set(map(int,input().split()))
    n = int(input())
    ts = set(map(int,input().split()))

    inter = st.intersection(ts)
    unite = st.union(ts)
    for i in inter:
        unite.discard(i)
    for i in unite:
        print (i)