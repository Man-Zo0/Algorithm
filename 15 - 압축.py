# https://programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer= []
    
    li = [chr(x) for x in range(65,91)]
    i = 0
    while i < len(msg):
        end = i+1
        while msg[i:end] in li:
            if end >= len(msg):
                end = len(msg) + 1
                break
            end += 1

        answer.append(li.index(msg[i:end-1])+1)
        li.append(msg[i:end])

        i += end-i -1
    return answer

msg = 'KAKAO'
print(solution(msg))