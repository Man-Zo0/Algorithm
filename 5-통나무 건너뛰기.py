#백준 11497
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,sys.stdin.readline().rstrip().split()))
    li.sort()

    a = []
    b = []

    for i in range(n):
        if i % 2 == 0:
            a.append(li[i])
        else:
            b.append(li[i])

    b.reverse()
    a += b

    r = abs(a[0]-a[n-1])

    for j in range(n-1):
        tmp = abs(a[j]-a[j+1])
        if  tmp > r:
            r = tmp

    print(r)
