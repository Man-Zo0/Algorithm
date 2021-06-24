n = int(input())
m = int(input())

mat = [[0 for _ in range(n)]for _ in range(n)]
visited = [0 for _ in range(n)]

for i in range(m):
    u,v = input().split()
    u,v = int(u)-1, int(v)-1
    mat[u][v] = 1
    mat[v][u] = 1

def dfs(mat,visited,n,v):
    visited[v] = True
    for w in range(n):
        if visited[w] == False and mat[v][w] == 1:
            dfs(mat,visited,n,w)

dfs(mat,visited,n,0)

print(visited.count(True)-1)
