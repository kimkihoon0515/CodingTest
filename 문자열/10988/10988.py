import sys

s = sys.stdin.readline().strip()

if s == s[::-1]:
    print('1')
else:
    print('0')