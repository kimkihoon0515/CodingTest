import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

while True:
    if len(s) == len(t): # 두 길이가 같지 않을때까지 반복
        break
    else:
        if t[-1] == 'A': # 가장 오른쪽 원소가 A면 제거
            t.pop()
        elif t[-1] == 'B': # 가장 오른쪽 원소가 B면 제거 후 뒤집기
            t.pop()
            t = list(reversed(t))

if s == t: 
    print(1)
else:
    print(0)