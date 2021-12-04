def solution(numbers):
    answer = ''
    n = list(map(str,numbers))
    n.sort(key = lambda x : x*3, reverse = True) # number의 원소가 1000 이하이므로 3번반복해서 큰 수 순으로 나열한다.
    # ex) 9,30,3이면 999,303030,333 이 되고 사전 순으로 333이 303030보다 크므로 3이먼저 오게된다.
    answer = str(int(''.join(n))) # 모든 원소를 순서대로 합치고 출력
    return answer