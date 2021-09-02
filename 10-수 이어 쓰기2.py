#백준 1790
import math
n,k = map(int,input().split())

def cal(n,k):
    if k >= 10:
        l = int(math.log10(n)) + 1
    else:
        l = 1
    
    lk = 1
    for i in range(1,l):
        tmp = i*9*(10**(i-1))
        if tmp < k:
            k -= tmp
            lk = i+1

    for i in range((10**(lk-1)),n+1):

        if k <= lk:
            print(list(str(i))[k-1])
            return
        
        k -= lk

    print(-1)

cal(n,k)