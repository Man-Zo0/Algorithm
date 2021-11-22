#https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations

def solution(orders, course):
    answer = []
    for cou in course:
        d = dict()
        for o in orders:
            tmp = list(combinations(sorted(o),cou))
            for tm in tmp:
                if tm not in d.keys():
                    d[tm] = 1
                else:
                    d[tm] += 1
        d = list(zip(d.keys(),d.values()))
        d.sort(key = lambda x: x[1], reverse = True)
        
        if len(d) < 1:
            break
        highest = d[0][1]
        if highest < 2:
            break
        for d_each in d:
            if d_each[1] == highest:
                answer.append("".join(d_each[0]))
            else:
                break
    return sorted(answer)