# 백준 1197

n,m = map(int,input().split())
li = []
for _ in range(m):
    u,v,cost = map(int,input().split())
    li.append([u,v,cost])
li.sort(key = lambda x : x[2])

#t = []
f = [0]

for i in range(1,n+1):
    f.append(i)

def find(u):
    if u != f[u]:
        f[u] = find(f[u])
    return f[u]

def union(u,v):
    r1 = find(u)
    r2 = find(v)
    f[r2] = r1

edge, r = 0,0

while True:
    if edge == n-1:
        break
    u,v,co = li.pop(0)
    if find(u) != find(v):
        union(u,v)
        #t.append((u,v))
        r += co
        edge += 1
    #print(f,r)
print(r)