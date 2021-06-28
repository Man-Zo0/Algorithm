#이코테 96p

n,m = map(int,input().split())

li=[]

for _ in range(n):
    li.append([int(x) for x in input().split()])

mini = []

for i in range(n):
    mini.append(min(li[i]))

print(max(mini))