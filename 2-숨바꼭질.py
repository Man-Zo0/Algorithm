start,end = [int(x) for x in input().split()]
li = []
visited = set()

def find(start,end):
    
    li.append([start])
    cnt = 0

    if start == end:
        return 0

    while True:
        li.append([])

        for i in li[cnt]:
            if i-1 == end or i+1 == end or i*2 == end:
                return cnt+1
            if i-1 not in visited and i-1>0:
                li[cnt+1].append(i-1)
                visited.add(i-1)
            if i<end:
                if i+1 not in visited:
                    li[cnt+1].append(i+1)
                    visited.add(i+1)
                if i*2 not in visited:
                    li[cnt+1].append(i*2)
                    visited.add(i*2)
        cnt += 1

print(find(start,end))


        



