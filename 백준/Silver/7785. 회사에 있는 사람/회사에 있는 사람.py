import sys

n = int(sys.stdin.readline().strip())

entry = {}

for _ in range(n):
    w = sys.stdin.readline().rstrip()
    if w.split()[1] == 'enter':
        entry[w.split()[0]] = 1
    elif w.split()[1] == 'leave':
        entry[w.split()[0]] -=1

ans = []
for key,value in entry.items():
    if value >0 :
        ans.append(key)

ans = sorted(ans,reverse=True)
for i in ans:
    print(i)
    