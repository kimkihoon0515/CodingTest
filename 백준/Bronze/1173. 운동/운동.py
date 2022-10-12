import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
sec, sec_exercise = 0, 0  
now = m

if now > M or now + T > M: 
    print(-1)
    sys.exit()

while sec_exercise < N:
    if now + T <= M:
        now += T
        sec += 1
        sec_exercise += 1
        continue
    else:
        while now + T > M:
            now -= R
            if now < m:   
                now = m
            sec += 1
print(sec)
