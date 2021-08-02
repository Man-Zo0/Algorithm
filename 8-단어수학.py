#백준 1339
n = int(input())
li = []
sum = dict()

for _ in range(n):
    li.append(input())

li.sort(key=lambda x: len(x),reverse=True)

for sentence in li:
    l = len(sentence)
    for i in range(l):
        val = 10**(l - i -1)

        if sentence[i] not in list(sum.keys()):
            sum[sentence[i]] = val
        else:
            sum[sentence[i]] += val

sum = sorted(sum.values(),reverse=True)

multi = 9
r = 0
for i in sum:
    r += i*multi
    multi -= 1

print(r)
