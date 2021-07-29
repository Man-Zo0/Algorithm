#백준 12904
s = list(input())
t = list(input())

ls = len(s)
lt = len(t)

found = False
while ls <= lt:

    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t.reverse()
    lt -= 1

    if s == t:
        found = True
        break

if found:
    print(1)
else:
    print(0)
