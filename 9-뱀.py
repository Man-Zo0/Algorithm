import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

mat = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    u,v = map(int,input().split())
    mat[u-1][v-1] = 2

seconds = []
directions = []
l = int(input())

for _ in range(l):
    o,p = input().split()
    seconds.append(int(o))
    directions.append(p)

sec = 0
dir = 1 # 0:위 1:우 2:아래 3:좌
mat[0][0] = 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]
x, y = 0,0

snake = [[0,0]]

while True:
    if sec in seconds:
        d = directions[seconds.index(sec)]
        if d == 'D':
            dir += 1
            if dir >= 4:
                dir = 0
        if d == 'L':
            dir -= 1
            if dir < 0:
                dir = 3    

    nextx = x + dx[dir]
    nexty = y + dy[dir]

    if nextx < 0 or nextx >= n or nexty < 0 or nexty >= n:
        break

    if mat[nexty][nextx] == 1:
        break
    elif mat[nexty][nextx] == 2:
        mat[nexty][nextx] = 1
        snake.append([nexty,nextx])
    else:
        mat[nexty][nextx] = 1
        snake.append([nexty,nextx])
        a,b = snake.pop(0)
        mat[a][b] = 0

    x = nextx
    y = nexty
    
    sec += 1

print(sec+1)
        