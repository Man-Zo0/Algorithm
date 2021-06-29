#이코테 118p

n,m = map(int,input().split())
a,b,d = map(int,input().split())

mat = []

for _ in range(n):
    mat.append(list(map(int,input().split())))

cnt = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while True:
    moved = False
    for _ in range(4):
        d -= 1
        if d < 0:
            d = 3

        nx = dx[d]+b
        ny = dy[d]+a
        
        if 0 < nx < n and 0 < ny < m:
            if mat[ny][nx] == 0:
                mat[ny][nx] = 1
                a = ny
                b = nx
                moved = True
                cnt += 1
                break
    if not moved:
        nx = b - dx[d]
        ny = a - dy[d]
        if 0 < nx < n and 0 < ny < m:
            if mat[ny][nx] == 1:
                break
            else:
                a = ny
                b = nx
        else:
            break
    
print(cnt)
