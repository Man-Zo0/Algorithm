import sys

n = int(input())

li = []

for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))

d = [0 for _ in range(n)]

d[0] = li[0]
if n>1:
    d[1] = li[0]+li[1]

for i in range(2,n):

    d[i] = max(d[i-3]+li[i-1]+li[i],d[i-2]+li[i])

print(d[n-1])
