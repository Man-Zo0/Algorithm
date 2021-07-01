#이코테 149p
from collections import deque

n,m = map(int,input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int,input())))


visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 0
r=[]

def bfs(x,y):
    queue = deque([[y,x]])
    visited[y][x] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            nx = v[1] + dx[i]
            ny = v[0] + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and mat[ny][nx] == 0:
                    queue.append([ny,nx])
                    visited[ny][nx] = True

for i in range(n):
    for j in range(m):
        if mat[i][j] == 0 and not visited[i][j]:
            bfs(j,i)
            cnt += 1

print(cnt)

