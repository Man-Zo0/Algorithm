import heapq 
import sys

n, m = map(int,sys.stdin.readline().strip().split())

graph = [[] for i in range(n + 1)]
distance = [-1] * (n + 1)
 
for _ in range(m):
    a, b, c = map(int , sys.stdin.readline().strip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start,end = map(int,sys.stdin.readline().strip().split())

for i in graph:
    i.sort(reverse=True, key=lambda x: x[1])

""" def dijkstra (start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q: 
        dist , now = heapq.heappop(q)
         
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist > 0:
                cost = min(dist,i[1])
            else: 
                cost = i[1]
            if cost > distance[i[0]]: 
                distance[i[0]] = cost 
                heapq.heappush(q,(cost, i[0])) """

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        dist = -dist
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist > 0:
                cost = min(dist, i[1])
            else:
                cost = i[1]
            if cost > distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (-cost, i[0]))
            if now == end:
                print(distance[end])
                return

dijkstra(start)

