import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

if a * len(b) == b * len(a):
    print(1)
else:
    print(0)