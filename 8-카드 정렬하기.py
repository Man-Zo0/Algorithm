#백준 1715
import heapq
n = int(input())
li = []
for _ in range(n):
    heapq.heappush(li,int(input()))

r = 0
if n == 1:
    print(0)
else:
    while len(li) > 1:
        first = heapq.heappop(li)
        second = heapq.heappop(li)

        r += first + second
        heapq.heappush(li,first+second)

    print(r)
