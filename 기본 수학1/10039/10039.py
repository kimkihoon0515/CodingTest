import sys

num = [int(sys.stdin.readline().strip()) for _ in range(5)]

for i in range(5):
    if num[i] <= 40:
        num[i] = 40

print(sum(num)//5)
