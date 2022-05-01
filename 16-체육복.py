#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    cnt = 0
    lost.sort()
    reserve.sort()
    
    tmp = []
    for l in lost:
        found = False
        for i in range(len(reserve)):
            if reserve[i] == l:
                reserve.pop(i)
                cnt += 1
                found = True
                break
        if not found:
            tmp.append(l)
                
    for l in tmp:
        for i in range(len(reserve)):
            if abs(reserve[i]-l) == 1:
                reserve.pop(i)
                cnt += 1
                break
    
    return n - len(lost) + cnt