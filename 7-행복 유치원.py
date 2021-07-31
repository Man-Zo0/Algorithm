#백준 13164
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

li = [int(x) for x in input().split()]

li = list(set(li))
li.sort()
n = len(li)

sub = []
for i in range(n-1):
    sub.append(li[i+1] - li[i])
sub.sort(reverse=True)

r = li[-1] - li[0]
for i in range(k-1):
    r -= sub[i]

print(r)
