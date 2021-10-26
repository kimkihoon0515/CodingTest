import sys

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

for i in range(len(li)): # li의 길이만큼 반복문돌려서 a에 있으면 1을 없으면 0을 출력한다.
    if li[i] in a:
        print(1)
    else:
        print(0)