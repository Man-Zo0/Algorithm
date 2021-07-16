n,k = map(int,input().split())

li = []

v = []
w = []

d = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)

def search(num,weight):

    if d[num][weight] > 0:
        return d[num][weight]

    if num == n:
        return 0

    include = 0
    if weight + w[num] <= k:
        include = v[num] + search(num+1,weight+w[num])
    exclude = search(num+1,weight)       

    d[num][weight] = max(include,exclude)
    return d[num][weight]

print(search(0,0))



