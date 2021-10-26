n = int(input()) # 도시의 개수
road = list(map(int,input().split())) # 각 도시간 거리
price = list(map(int,input().split())) # 각 도시의 기름 값


result = 0 # 결과값을 저장하는 변수
minimum = price[0] # 최소값을 저장하는 변수
for i in range(len(road)): # 반복문을 돌려서 그 도시의 기름값이 현재의 최소값보다 크면 결과에 현재의 최소값 * 도로의 길이를 더해준다.
    if price[i] >= minimum:
        result += minimum * road[i]
    else: # 기름값의 최소값이 갱신되면 결과값에 도로의 길이 * 기름의 최소값을 더해준다.
        minimum = price[i]
        result += minimum * road[i]
print(result)
