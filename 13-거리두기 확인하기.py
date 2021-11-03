#https://programmers.co.kr/learn/courses/30/lessons/81302
def solution(places):
    ans = [1,1,1,1,1]
    dx,dy = [1,0,-1,0], [0,1,0,-1]
    cnt = 0
    for p in places:
        tf = 1
        
        for y in range(5):
            for x in range(5):
                if p[y][x] == 'P':
                    #상하좌우
                    for k in range(4):
                        nx,ny = x + dx[k], y + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if p[ny][nx] == 'P':
                                tf = 0
                                break
                            elif p[ny][nx] == 'O':
                                for i in range(4):
                                    nnx, nny = nx + dx[i], ny + dy[i]
                                    if 0 <= nnx < 5 and 0 <= nny < 5 and not (nnx == x and nny == y):
                                        if p[nny][nnx] == 'P':
                                            tf = 0 
                                            break
        ans[cnt] = tf
        cnt += 1
    return ans