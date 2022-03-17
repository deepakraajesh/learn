from collections import Counter

def matchingStrings(strings, queries):
    s = Counter(strings)
    for i in range(len(queries)):
        if queries[i] in s:
            print(s.get(queries[i]))
        else:
            print("0")

if __name__ == '__main__':
    strings_count = int(input().strip())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res = matchingStrings(strings, queries)