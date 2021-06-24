n = int(input())
cnt = 0

mat = []
r = []
visited = [[False for _ in range(n)]for _ in range(n)]

for i in range(n):
    mat.append([int(x) for x in list(input())])

def find(mat,r,visited,n,row,col):
    visited[row][col] = True
    if col<n-1:
        if mat[row][col+1] == 1 and visited[row][col+1] == False:
            r[cnt] += 1
            find(mat,r,visited,n,row,col+1)
    if col>0:
        if mat[row][col-1] == 1 and visited[row][col-1] == False:
            r[cnt] += 1
            find(mat,r,visited,n,row,col-1)
    if row<n-1:
        if mat[row+1][col] == 1 and visited[row+1][col] == False:
            r[cnt] += 1
            find(mat,r,visited,n,row+1,col)
    if row>0:
        if mat[row-1][col] == 1 and visited[row-1][col] == False:
            r[cnt] += 1
            find(mat,r,visited,n,row-1,col)

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1 and visited[i][j] == False:
            r.append(1)
            find(mat,r,visited,n,i,j)
            cnt += 1

r.sort(reverse=True)
print(len(r))

for _ in range(len(r)):
    print(r.pop())

