import sys

s = sys.stdin.readline().strip()


for i in range(0,len(s),10):
    a = i + 10
    print(s[i:a])
