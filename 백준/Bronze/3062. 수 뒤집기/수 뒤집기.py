import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a = sys.stdin.readline().strip()
    b = int(a) + int(a[::-1])
    if str(b) == str(b)[::-1]:
        print('YES')
    else:
        print('NO')