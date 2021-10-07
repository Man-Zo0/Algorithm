#프로그래머스
def solution(lines):
    ans = 0
    li = []
    se = set()
    for l in lines:
        trash, time, duration = l.split()
        h,m,s = time.split(":")
        
        end = float(s) + int(m)*60 + int(h)*3600
        start_tmp = end - float(duration[:-1]) + 0.001
        start = round(start_tmp,3)
        li.append([start,end])
        print(start,end)
        se.add(start)
        se.add(end)
        
    li.sort()
    list(se).sort()
    
    for s in se:
        cnt = 0
        e = round((s + 0.999),3)
        print(s,e)
        
        for l in li:
            st = l[0]
            en = l[1]
            if st <= s <= en or st<= e <= en or (s<=st and en<= e):
                cnt += 1
                
        if cnt > ans:
            ans = cnt
    
    return ans