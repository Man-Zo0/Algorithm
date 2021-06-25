from typing import Deque
import sys

m,n = [int(x) for x in input().split()]
mat = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]
r = 0
cnt = 0

for i in range(n):
    mat.append([int(x) for x in sys.stdin.readline().split()])
    cnt += mat[i].count(0)

if cnt == 0:
    print(0)
else:
    tmp = [] 
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                tmp.append([(i,j)])

    while True:
        tmp.append([])
        for point in tmp[r]:
            for k in range(4):
                newx = point[1] + dx[k]
                newy = point[0] + dy[k]

                if 0<=newx<m and 0<=newy<n:
                    if mat[newy][newx] == 0 and (newy,newx) not in tmp[r+1]:
                        tmp[r+1].append((newy,newx))

        for u in tmp[r+1]:
            mat[u[0]][u[1]] = 1 
            cnt -= 1
            
        if cnt == 0:
            r+=1
            break
        if len(tmp[r+1]) != 0:
            r+=1
        else:
            r = -1
            break

    print(r)



