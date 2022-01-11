import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline()
    li = s.split(',')
    sum = int(li[0])+int(li[1])
    print(sum)