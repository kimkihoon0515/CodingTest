import sys

while True:
    n,m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    cd1 = [int(sys.stdin.readline().strip()) for _ in range(n)]
    cd2 = [int(sys.stdin.readline().strip()) for _ in range(m)]

    left = 0
    right = 0
    cnt = 0

    while left < n and right < m:
        if cd1[left] == cd2[right]:
            cnt +=1
            left +=1
            right +=1
        elif cd1[left] > cd2[right]:
            right +=1
        else:
            left +=1

    print(cnt)