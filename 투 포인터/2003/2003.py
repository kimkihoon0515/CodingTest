import sys

n,m = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

result = 0
sum = 0
end = 0

for start in range(n):
    while sum < m and end < n: # sum이 m보다작고 end 가 배열 길이보다 작으면
        sum +=li[end] # end를 하나씩 늘려가면서 합계에 더해간다.
        end +=1
    if sum == m: # m 과 합계가 같아지면
        result +=1 # 개수 1 증가시키고
    sum -= li[start] # 시작점의 데이터를 빼준다.

print(result)