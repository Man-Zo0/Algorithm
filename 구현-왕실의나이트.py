#이코테 115p

st = input()
col,row = ord(st[0])-96,int(st[1])

dx = [-1,1,2,2,-1,1,-2,-2]
dy = [2,2,1,-1,-2,-2,1,-1]
cnt = 0

for i in range(8):
    if 0 < col + dx[i] < 9 and 0 < row + dy[i] < 9:
        cnt += 1

print(cnt)

