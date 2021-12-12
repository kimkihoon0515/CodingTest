import sys

n,m = map(int,sys.stdin.readline().split())

t = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = 0
right = max(t)*m # 심사관들에게 주어진 시간이 가장 클 경우

while left <= right:
    mid = (left+right)//2 # 모든 심사관들에게 주어진 시간
    people = sum(mid//i for i in t) # 모든 심사관들이 주어진 시간동안 심사 가능한 사람들의 명수를 합친 것
    if people >= m :
        answer = mid
        right = mid-1
    else:
        left = mid +1
print(answer)