#https://programmers.co.kr/learn/courses/30/lessons/17686
def solution(files):
    li = []
    for f in range(len(files)):
        head = ''
        headavailable = True
        numberavailable = True
        number = ''
        cnt = 0
        for word in files[f]:
            if 'a' <= word <= 'z' or 'A' <= word <= 'Z' or word in '.-' or word == ' ':
                if headavailable:
                    head += word.upper()
                else:
                    numberavailable = False
            else:
                headavailable = False
                if numberavailable:
                    number += word
                cnt += 1
                if cnt >= 5:
                    break
        li.append([head,int(number),f,files[f]])
    li.sort()
    print(li)
    return [x[3] for x in li]