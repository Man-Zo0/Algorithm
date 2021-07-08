#백준 15686
from itertools import combinations

n,m = map(int,input().split())

home = []
store = []

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 2:
            store.append([i,j])
        elif row[j] == 1:
            home.append([i,j])

comb = combinations(store,m)

r = 99999
for i in comb:
    total = 0
    for h in home:
        dist = 99999
        for s in i:
            tmp = abs(h[0]-s[0])+abs(h[1]-s[1])
            if dist > tmp:
                dist = tmp
        total += dist
    if r > total:
        r = total

print(r)


