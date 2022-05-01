#https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    ans = 0
    for i in range(left,right+1):
        n = yaksu(i)
        if n%2 == 0:
            ans += i
        else:
            ans -= i
            
    return ans

def yaksu(n):
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt += 1
    return cnt