def bigSorting(unsorted):
    unsorted.sort(key=int)
    for s in unsorted:
        print(s)

if __name__ == '__main__':
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    bigSorting(unsorted)