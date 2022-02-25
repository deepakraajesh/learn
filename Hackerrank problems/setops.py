if __name__ == "__main__":
    m = int(input())
    s = set([])
    for i in range (0,m):
        s.add(input())
    n = int(input())
    t = set([])
    for j in range (0,n):
        t.add(input())

    intersect = s.intersection(t)
    unite = s.union(t)
    for k in intersect:
        unite.discard(k)
    for p in unite:
        print(p)