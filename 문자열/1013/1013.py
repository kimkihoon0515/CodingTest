import sys
import re

t = int(sys.stdin.readline())

def pattern(s):
    p = re.compile('(100+1+|01)+') # (100+1+|01)+ 을 패턴 객체로 반환한다.
    result = p.fullmatch(s) # 패턴이 정확히 맞아 떨어지는지 결과값 반환
    if result:
        print('YES')
    else:
        print('NO')

for _ in range(t):
    s = sys.stdin.readline().strip()
    pattern(s)

