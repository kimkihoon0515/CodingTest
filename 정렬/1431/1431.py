import sys

n = int(sys.stdin.readline())

def num(s):
    result = 0
    for i in s:
        if i.isdigit():
            result += int(i)
    return result

s = [sys.stdin.readline().strip() for _ in range(n)]
s = sorted(s,key=lambda x: (len(x),num(x),x))

for i in s:
    print(i)