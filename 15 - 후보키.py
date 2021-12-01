# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations
def solution(relation):
    collen = len(relation[0])
    answer = []
    columns = [[] for x in range(collen)] 
    
    for i in range(len(relation)):
        for j in range(collen):
            columns[j].append(relation[i][j]) 
            
    for i in range(collen):
        if len(columns[i]) == len(set(columns[i])):
            answer.append([i])
            
    for i in range(2,collen+1):
        combs = list(combinations([x for x in range(collen)], i))
        for comb in combs:
            minimality = True
            for ans in answer:
                if set(ans) & set(comb) == set(ans):
                    minimality = False
            if not minimality:
                continue
            
            li = [[] for x in range(len(relation))]
            for j in range(len(relation)):
                for c in comb:
                    li[j].append(relation[j][c])
                li[j] = str(li[j])
            
            if len(li) == len(set(li)):
                answer.append(comb)
                
    return len(answer)