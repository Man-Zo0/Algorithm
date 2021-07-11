n,m = map(int,input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

d = [999] * (m+1)

coin.sort()

d[0] = 0
for i in range(1,coin[0]):
    d[i] = 0

for i in range(coin[0],m+1):
    for j in coin:
        if i >= j:
            d[i] = min(d[i],d[i-j]+1)

print(d[m])