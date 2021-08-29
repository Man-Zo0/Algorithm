#백준 2564
m, n= map(int,input().split())
k = int(input())
li = []
rect = 2* (n+m)

for _ in range(k+1):
    dir, pos = map(int,input().split())
    if dir == 1:
        li.append(m-pos)
    elif dir == 3:
        li.append(m+pos)
    elif dir == 2:
        li.append(m+n+pos)
    else:
        li.append(n+(2*m)+n-pos)

x = li.pop()

r = 0
for i in li:
    tmp = abs(x-i)
    r += min(tmp, rect - tmp)

print(r)