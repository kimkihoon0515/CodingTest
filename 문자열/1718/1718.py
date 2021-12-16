import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

answer = ''

for i in range(len(s)):
    if s[i] == ' ':
        answer += ' '
    else:
        answer += chr((ord(s[i])-ord(t[i%len(t)])-1) % 26 + ord('a'))

print(answer)