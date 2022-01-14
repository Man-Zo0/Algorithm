#https://programmers.co.kr/learn/courses/30/lessons/12973
from collections import deque

def solution(s):
    stack = deque()
    
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return int( len(stack) == 0)
