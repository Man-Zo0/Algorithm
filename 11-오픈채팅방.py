#프로그래머스
def solution(record):
    li = dict()
    users = set()
    ans = []
    
    for r in record:
        tmp = r.split()
        ty = tmp[0]
        
        if ty == "Enter":
            user = tmp[1]
            name = tmp[2]
            
            if user not in users:
                users.add(user)
            li[user] = name
        
        elif ty == "Change":
            user = tmp[1]
            name = tmp[2]
            
            li[user] = name
    
    for r in record:
        tmp = r.split()
        ty = tmp[0]
        
        if ty == "Enter":
            ans.append(li[tmp[1]]+"님이 들어왔습니다.")
        elif ty == "Leave":            
            ans.append(li[tmp[1]]+"님이 나갔습니다.")
            
    return ans