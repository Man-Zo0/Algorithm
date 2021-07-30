#백준 1753
import sys
import heapq

n,e = map(int,sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)

for _ in range(e):
    u,v,w = map(int,sys.stdin.readline().strip().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)

for d in range(1,n+1):
    if distance[d] >= int(1e9):
        print('INF')
    else:
        print(distance[d])
