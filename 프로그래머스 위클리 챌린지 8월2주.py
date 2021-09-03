def solution(scores):
    l = len(scores)
    r = [0 for x in range(l)]
    
    print(l)
    rev = [] * (l+1)
    print(rev)

    for i in range(l):
        for j in range(l):
            rev[j].append(scores[i][j])

    print(rev)
