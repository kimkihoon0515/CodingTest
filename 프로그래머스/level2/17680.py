def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [i.lower() for i in cities] # 대소문자 구별 없애기 위해 소문자로 변경
    if cacheSize == 0: # cacheSize가 0이면 무조건 5씩 증가하므로 
        answer = 5 * len(cities)
    else:
        for city in cities: 
            if len(cache) < cacheSize: # cacheSize에 다 못채운 경우
                if city in cache: # cache가 가득차지 않은 상태에서 cache hit 인 경우
                    cache.append(city)
                    answer += 1
                else: # cache가 가득차지 않은 상태에서 cache miss인 경우
                    cache.append(city)
                    answer += 5
            else:
                if city in cache: # cache가 가득 찬 상태에서 cache hit인 경우
                    cache.pop(cache.index(city))
                    cache.append(city)
                    answer += 1
                else: # cache가 가득 찬 상태에서 cache hit이 아닌 경우
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
    return answer