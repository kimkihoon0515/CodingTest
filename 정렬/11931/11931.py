import sys

n = int(sys.stdin.readline())

num = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)),reverse=True)

for i in num:
    print(i)

