#백준 3079
import sys

n,m = map(int,sys.stdin.readline().strip().split())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))

r = 0

def search(start,end,target):
    global r
    while start <= end:

        mid = (start + end) // 2

        sum = 0
        for i in li:
            sum += mid // i

        if sum >= target: #이게 핵심
            r = mid
            end = mid - 1
        else:
            start = mid + 1

search(0,min(li)*m,m)
print(r)

""" 삽질 코드
def search(start,end,target):
    if start>end:
        return

    mid = (start + end) // 2

    sum = 0
    divided = 0
    for i in li:
        if i <= mid:
            sum += mid // i
            if mid % i == 0:
                divided += 1
        else:
            break

    if sum >= target >= sum-divided:
        while mid > 0:
            for j in check:
                if mid % j == 0:
                    print(mid)
                    return
            mid -= 1
    elif sum > target:
        search(start,mid-1,target)
    else:
        search(mid+1,end,target)

search(0,li[0]*m,m) """