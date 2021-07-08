# 백준 2660 플로이드와샬?
from collections import deque

n = int(input())

mat = [[] for _ in range(n+1)]

while True:
    u,v = map(int,input().split())

    if u == -1:
        break
    else:
        mat[u].append(v)
        mat[v].append(u)

def bfs(u):
    maxcost = 0
    queue = deque([[u,0]])
    visited = [False for _ in range(n+1)]
    visited[u] = True

    while queue:
        v,cost = queue.popleft()
        if cost > maxcost:
            maxcost = cost

        for node in mat[v]:
            if not visited[node]:
                queue.append([node,cost+1])
                visited[node] = True
    return maxcost

score = []
for i in range(n):
    score.append(bfs(i+1))
r=[]
mini = min(score)
for s in range(len(score)):
    if score[s] == mini:
        r.append(s)

print(mini,len(r))

for i in r:
    print(i+1,end=' ')
