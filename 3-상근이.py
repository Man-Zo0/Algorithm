def find(u):
    if u != f[u]:
        f[u] = find(f[u])
    return f[u]

def union(u,v):
    r1 = find(u)
    r2 = find(v)
    f[r2] = r1

case = int(input())
r = []

for _ in range(case):
    n,m = map(int,input().split())
    li = []
    for _ in range(m):
        li.append(map(int,input().split()))
    
    f = [0]
    for i in range(1,n+1):
        f.append(i)

    edge, cost = 0,0

    while True:
        if edge == n-1:
            break
        u,v = li.pop(0)
        if find(u) != find(v):
            union(u,v)
            cost+=1
            edge+=1

    r.append(cost)

for rr in r:
    print(rr)