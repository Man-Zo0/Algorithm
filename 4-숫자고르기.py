# 백준 2688

n = int(input())

li = [0]
for _ in range(n):
    li.append(int(input()))

def search(i,ind,val):
    global r
    ind.add(i)
    val.add(li[i])

    if (val == ind):
        r = r|ind
        return
    else:
        if li[i] not in ind:
            search(li[i],ind,val)
        else:
            return

r = set()
for i in range(1,n+1):
    ind = set()
    val = set()

    tmp = search(i,ind,val)

print(len(r))

r = list(r)
r.sort()

for i in r:
    print(i)
