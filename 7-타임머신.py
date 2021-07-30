#백준 11657
import  sys
input = sys.stdin.readline

n,m = map(int,input().split())
li = []
distance = [float('inf')] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    li.append((a,b,c))

def bf(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur = li[j][0]
            next = li[j][1]
            cost = li[j][2]

            if distance[cur] != float('inf') and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == n-1:
                    return True
    return False

neg = bf(1)

if neg:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] >= float('inf'):
            print(-1)
        else:
            print(distance[i])

