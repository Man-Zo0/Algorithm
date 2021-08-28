#백준 14500
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def search(n,m,cnt,r,y,x,visited):
    global ans

    r += mat[y][x]
    visited[y][x] = 1

    if cnt >= 3:
        if r > ans:
            ans = r
        return

    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < m and 0 <= newy < n and not visited[newy][newx]:
            search(n,m,cnt+1,r,newy,newx,visited)
            visited[newy][newx] = 0
ans = 0
for i in range(n):
    for j in range(m):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        search(n,m,0,0,i,j,visited)

for i in range(n):
    for j in range(m):
        tmp = []
        t = mat[i][j]
        for k in range(4):
            newx = j + dx[k]
            newy = i + dy[k]
            if 0 <= newx < m and 0 <= newy < n:
                tmp.append(mat[newy][newx])
        if len(tmp) > 2:
            tmp.sort(reverse=True)
            t += tmp[0]
            t += tmp[1]
            t += tmp[2]
        if t > ans:
            ans = t

print(ans)