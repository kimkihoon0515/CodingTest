import sys
input = sys.stdin.readline
s = []
for i in range(7):
    a = int(input())
    if a % 2 != 0: s.append(a)
if s:
    print(sum(s))
    print(min(s))
else:
    print(-1)