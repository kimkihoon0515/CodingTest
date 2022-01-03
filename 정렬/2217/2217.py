import sys

n = int(sys.stdin.readline())

rope = sorted([int(sys.stdin.readline()) for _ in range(n)])

answer = []
for i in range(len(rope)):
    answer.append(rope[i]*(n-i))

print(max(answer))