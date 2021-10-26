import sys
n = int(input())

list = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline())
    list[num] = list[num]+1

for i in range(10001):
    if list[i] !=0:
        for _ in range(list[i]):
            print(i)