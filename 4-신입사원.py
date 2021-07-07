#백준 1946

t = int(input())

for _ in range(t):
    n = int(input())

    li = []
    for _ in range(n):
        li.append(list(map(int,input().split())))
    
    li.sort(key= lambda r: r[0])

    cnt = 1
    compare = li[0]

    for i in range(1,n):
        if li[i][0] < compare[0] or li[i][1] < compare[1]:
            cnt += 1
            compare = li[i]
    
    print(cnt)