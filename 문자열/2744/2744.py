import sys

s = sys.stdin.readline().strip()

ans = ''
for i in range(len(s)):
    if s[i].islower():
        ans+=s[i].upper()
    else:
        ans += s[i].lower()
print(ans)