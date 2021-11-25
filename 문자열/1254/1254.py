import sys

s = sys.stdin.readline().strip()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break