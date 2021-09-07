import sys
N = int(sys.stdin.readline())
arr=[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
tmp=[0 for i in range(10)]

if N == 1:
    print(sum(arr))
else:
    for i in range(N-1):
        for j in range(10):
            if j == 0:
                tmp[0]=arr[1]
            elif j == 9:
                tmp[9]=arr[8]
            else:
                tmp[j]=arr[j-1]+arr[j+1]
        arr = tmp.copy()
    print(sum(arr)%1000000000)
# 상태공간트리 그려보면 패턴 파악 가능
# N번째 depth의 0의 개수는 N-1번째의 1의 개수
# N번째 depth의 1의 개수는 N-1번째의 0과 2의 개수
# N번째 depth의 2의 개수는 N-1번째의 1과 3의 개수
#....
# N번째 depth의 8의 개수는 N-1번째의 7과 9의 개수
# N번째 depth의 9의 개수는 N-1번째의 8의 개수