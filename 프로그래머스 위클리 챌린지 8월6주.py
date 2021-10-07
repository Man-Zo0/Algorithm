def solution(weights, head2head):
    li = []
    length = len(weights)
    for h in range(length):
        game = 0
        win = 0
        heavy = 0
        rate = 0
        for wl in range(length):
            if head2head[h][wl] == 'N':
                continue
            elif head2head[h][wl] == 'W':
                win += 1
                if weights[h] < weights[wl]:
                    heavy += 1
            game += 1
            if game == 0:
                rate = 0
            else:
                rate = win/game
        li.append([rate, heavy, weights[h], length - h ,h+1])
    
    li.sort(reverse=True)
    ans = [x[4] for x in li]
    return ans