import heapq
n = int(input())
h = []
heapq.heapify(h)
for i in range(n):
    s = list(input().split())
    if (s[0]=='1'):
        heapq.heappush(h,int(s[1]))
    if (s[0]=='2'):
        heapq.heappop(h)
    if (s[0]=='3'):
        print(h[0])

#To check how min heap, max heap, insert element in heap, delete (only root is possible in heap), priority queues, heap sort can be seen in this URL - https://www.youtube.com/watch?v=HqPJF2L5h9U