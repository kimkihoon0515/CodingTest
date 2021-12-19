import sys

while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        exit()
    if n == n[::-1]:
        print('yes')
    else:
        print('no')