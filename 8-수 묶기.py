#백준 1744
n  = int(input())
neg = []
pos = []

r = 0
for _ in range(n):
    i = int(input())
    if i > 1:
        pos.append(i)
    elif i < 1:
        neg.append(i)
    else:
        r += i
    
pos.sort(reverse=True)
neg.sort()

l= len(pos)
if l % 2 == 0:
    length = l
else:
    length = l - 1
    r += pos[-1]
for j in range(0,length,2):
    r += pos[j]*pos[j+1]

k = len(neg)
if k % 2 == 0:
    length2 = k
else:
    length2 = k - 1
    r += neg[-1]
for o in range(0,length2,2):
    r += neg[o]*neg[o+1]

print(r)
