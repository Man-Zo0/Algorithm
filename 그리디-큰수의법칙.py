# 이코테 92p

n, m, k = list(map(int,input().split()))

li = [int(x) for x in input().split()]

li.sort()
li.reverse()

r = 0
cnt = 0

for i in range(m):
    if cnt<k:
        r += li[0]
        cnt += 1
    else:
        r += li[1]
        cnt = 0
print(r)     
