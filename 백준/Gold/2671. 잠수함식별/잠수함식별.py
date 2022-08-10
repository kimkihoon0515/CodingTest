import sys

import re

s = str(sys.stdin.readline().strip())

# (100~1~|01)~ : 100~ 은 0이 x번 반복 가능 

pattern = re.compile('(100+1+|01)+')
answer = pattern.fullmatch(s)

if answer:
    print('SUBMARINE')
else:
    print('NOISE')