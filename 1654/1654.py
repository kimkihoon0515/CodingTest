import sys

k,n = map(int,sys.stdin.readline().split()) # k개의 랜선들을 잘라서 길이가 같은 n개의 랜선을 만들어야 한다.
li = []

for _ in range(k):
    li.append(int(sys.stdin.readline()))

li.sort()
""" 시간초과 발생 / 이분탐색으로 풀어야함
result = []
for i in range(1,li[-1]):
    sum = 0
    for j in li:
        sum += j // i
    if sum == n:
        result.append(i)
print(max(result))
"""

start,end = 1,li[-1]

while start <= end:
    mid = (start+end) //2
    sum = 0
    for i in li:
        sum += i // mid
    if sum >=n:
        start = mid +1
    else:
        end = mid -1
print(end)


""" 이분탐색 알고리즘 
def BinarySearch(arr, val, low, high):
    if low > high:
        return False #해당 배열에 타겟 숫자 미존재
    
    mid = (low + high) // 2 #위치 기반으로 찾는 것
    
    if arr[mid] > val:
        return BinarySearch(arr, val, low, mid - 1) #수가 중앙 값보다 아래 있는 경우
    elif arr[mid] < val:
        return BinarySearch(arr, val, mid + 1, high) #수가 중앙 값보다 위에 있는 경우
    else:
        return True #아니면 숫자를 출력 -> return val
"""