#백준 2170
import sys
n = int(input())

li = []
for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().rstrip().split())))

li.sort(key= lambda x:x[0])

r = 0
start,end = li[0][0],li[0][1]
for i in range(1,n):
    if li[i][0] <= end:
        if li[i][1] > end:
            end = li[i][1]
    else:
        r += end-start
        start = li[i][0]
        end = li[i][1]
r += end-start

print(r)

