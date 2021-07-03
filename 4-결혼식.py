#백준 5567

n = int(input())
m = int(input())

li = []
f = set()
r = set()
r.add(1)

for i in range(m):
    li.append(list(map(int,input().split())))

    if 1 in li[i]:
        f.add(li[i][0])
        f.add(li[i][1])
    
for i in range(m):
    for j in f:
        if j in li[i]:
            r.add(li[i][0])
            r.add(li[i][1])

print(len(r)-1)



