import sys
input = sys.stdin.readline

N = int(input())
cities = list(map(int, input().split()))
budgets = int(input()) # 예산
start, end = 0, max(cities) # 시작 점, 끝 점

# 이분 탐색
while start <= end:
    mid = (start+end) // 2
    total = 0 # 총 지출 양
    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= budgets: # 지출 양이 예산 보다 작으면
        start = mid + 1
    else: # 지출 양이 예산 보다 크면
        end = mid - 1
print(end)