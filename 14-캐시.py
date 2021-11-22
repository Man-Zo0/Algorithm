#https://programmers.co.kr/learn/courses/30/lessons/17680
def solution(cacheSize, cities):
    runtime = len(cities) * 5
    if cacheSize == 0:
        return runtime
    
    for city in range(len(cities)):
        cities[city] = cities[city].upper()
    
    li = []
    for city in cities:
        if city in li:
            li.append(li.pop(li.index(city)))
            runtime -= 4
        else:
            if len(li) < cacheSize:
                li.append(city)
            else:
                li.pop(0)
                li.append(city)
    
    return runtime