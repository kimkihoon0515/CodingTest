import sys

n,m = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

li.sort()
start = 1
end = li[-1]

while start <= end:
    mid = (start + end) //2 # 첫 중앙값을 1과 최대값으로 정하고 거기서 조건에 맞지 않을때마다 조정해나가는 방식.
    sum = 0
    for i in li:
        if mid <= i: # i보다 작으면 
            sum += (i-mid) # 나무를 베서 잘려진 높이를 합계에 더해준다.
    if sum >= m:
        start = mid +1 #  sum이 m보다 크면 최소값이었던 1을 mid+1로 옮긴다.
    else: # 만약 나무길이가 m보다 작으면 end를 조절한다.
        end = mid -1
print(end)

        