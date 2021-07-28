#백준 9084
t = int(input())

for _ in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]

    m = int(input())

    d = [0] * (m+1)

    d[0] = 1
    for i in range(1,li[0]):
        d[i] = 0

    for j in li:
        for i in range(j,m+1):
                d[i] += d[i-j] 

    print(d[m])