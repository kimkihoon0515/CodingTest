import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    s = sys.stdin.readline().split()
    ans = ''
    for i in s:
        ans += i[::-1]
        ans += ' '
    print(ans.strip())