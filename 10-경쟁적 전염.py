#백준 18405
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
mat = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    mat.append([int(x) for x in input().split()])

s,ry,rx = map(int,input().split())

que = []
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            que.append((mat[i][j],j,i,0))
que.sort()

cur = 0
while que:
    val, x, y, sec = que.pop(0)

    if cur == s:
        break

    if cur < sec:
        que.append((val,x,y,sec))
        que.sort()
        cur += 1
        continue


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <n and 0 <= ny < n:
            if not mat[ny][nx]:
                mat[ny][nx] = val
                que.append((val,nx,ny,sec+1))

print(mat[ry-1][rx-1])