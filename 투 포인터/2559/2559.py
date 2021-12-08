import sys

n,k = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

sum = 0
end = 0
result = [] # 결과 배열
for start in range(n):
    while end < n and end < start + k: # 배열 길이보다 작고 구간의 크기가 2가 되기 전까지 반복문을 돌린다.
        sum += li[end] # 구간의 합을 저장해놓고
        end +=1 # 끝 주소를 하나씩 증가
    if end == start + k: # 구간의 길이가 2가 되면
        result.append(sum) # 결과배열에 넣고
    sum -= li[start] # 시작주소의 데이터값을 합에서 뺀다.

print(max(result)) # 최대값 출력