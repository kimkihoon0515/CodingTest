import sys

s = sys.stdin.readline().strip()

w = sys.stdin.readline().strip()

cnt = 0

n = 0

while n <= len(s) - len(w):
    if s[n:n+len(w)] == w: # 범위를 지정해서 그 범위랑 w랑 같으면 cnt를 1개씩 늘려간다.
        cnt +=1
        n += len(w) # 시작점을 비교하려는 w만큼 옮겨준다.
    else:
        n+=1 # 첫번째 글자부터 다르면 한칸씩만 움직인다.
print(cnt)