#프로그래머스
def solution(lottos, win_nums):
    already, zero = 0,0
    for i in lottos:
        if i in win_nums:
            already += 1
        elif i == 0:
            zero +=1
    mini = 7 - already 
    maxi = 7 - already - zero 
    if maxi > 6:
        maxi = 6
    if mini > 6:
        mini = 6
    return [maxi,mini]