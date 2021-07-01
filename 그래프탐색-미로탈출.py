#이코테 152p
from collections import deque

n,m = map(int,input().split())
mat = []

for _ in range(n):
    mat.append(list(map(int,input())))

visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    queue = deque([[0,0,1]])
    visited[0][0] = True

    while queue:
        y,x,cost = queue.popleft()

        if y == n-1 and x == m-1:
            return cost

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n:
                if mat[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append([ny,nx,cost+1])
                    visited[ny][nx] = True

print(bfs())