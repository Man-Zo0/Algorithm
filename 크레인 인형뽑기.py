#https://programmers.co.kr/learn/courses/30/lessons/64061
from collections import deque

def solution(board, moves):
    stack = deque([0])
    length = len(board)
    answer = 0

    for move in moves:
        for i in range(length):
            if board[i][move-1] != 0:
                holding = board[i][move-1] 
                board[i][move-1] = 0

                if stack[-1] == holding:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(holding)
                
                break
    
    return answer

b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
print(solution(b,m))