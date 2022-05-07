import sys

s = sys.stdin.readline().strip()

answer = ''
for i in s:
    if i.isupper():
        answer += i
print(answer)