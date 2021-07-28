#백준 3020
import sys
from bisect import bisect_left

n,h = map(int,sys.stdin.readline().strip().split())

up = []
down = []

for i in range(n):
    if i % 2 == 0:
        down.append(int(sys.stdin.readline().strip()))
    else:
        up.append(int(sys.stdin.readline().strip()))
    
down.sort()
up.sort()

def search():
    mini = float('inf')
    cnt = 1

    for height in range(1,h+1):
        up_index = bisect_left(up,h-height+1)
        down_index = bisect_left(down,height)

        destroy = n - (up_index + down_index) 
        if destroy < mini:
            mini = destroy
            cnt = 1
        elif destroy == mini:
            cnt += 1

    return mini,cnt

print(*search())
        


    
