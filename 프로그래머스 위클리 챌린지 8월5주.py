def solution(word):
    li = ['A']
    w = ['A']
    l = 0
    
    first = ['A','E','I','O']
    second = ['E','I','O','U']
    
    while True:
        if l < 4:
            w.append('A')
            l += 1
        else:
            if w[l] in first:
                w[l] = second[first.index(w[l])]
            else:
                while w[l] == 'U':
                    w.pop()
                    l -= 1
                    if l < 0:
                        return li.index(word)+1

                w[l] = second[first.index(w[l])]
        li.append("".join(w))