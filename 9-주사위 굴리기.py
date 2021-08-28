import sys
input = sys.stdin.readline

n,m,y,x,k = map(int,input().split())

mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

order = [int(x) for x in input().split()]

dice = [[0,0,0,0],[0,0,0]]

def afterroll(y,x):
    if mat[y][x] == 0:
        mat[y][x] = dice[0][3]
    else:
        dice[0][3] = mat[y][x]
        mat[y][x] = 0

    print(dice[0][1])

for i in range(k):
    ord = order[i]

    if ord == 1:
        if x != m-1:
            tmp = dice[0][1]
            dice[0][1] = dice[1][0]
            dice[1][1] = dice[1][0]
            dice[1][0] = dice[0][3]
            dice[0][3] = dice[1][2]
            dice[1][2] = tmp

            x += 1
            afterroll(y,x)
    
    elif ord == 2:
        if x != 0:
            tmp = dice[0][1]
            dice[0][1] = dice[1][2]
            dice[1][1] = dice[1][2]
            dice[1][2] = dice[0][3]
            dice[0][3] = dice[1][0]
            dice[1][0] = tmp

            x -= 1
            afterroll(y,x)

    elif ord == 3:
        if y != 0:
            tmp = dice[0][0]
            dice[0][:-1] = dice[0][1:]
            dice[0][3] = tmp

            y -= 1
            afterroll(y,x)
    
    elif ord == 4:
        if y != n-1:
            tmp = dice[0][3]
            dice[0][1:] = dice[0][:-1]
            dice[0][0] = tmp

            y += 1
            afterroll(y,x)


    
