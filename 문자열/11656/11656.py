import sys

s = sys.stdin.readline().strip()

answer = []

for i in range(len(s)):
    answer.append(s[i:])

answer = sorted(answer)
for i in answer:
    print(i)