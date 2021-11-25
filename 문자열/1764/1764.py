""" 시간초과 오류발생
import sys

n,m = map(int,sys.stdin.readline().split())

no_see = []

no_hear = []

for _ in range(n):
    no_see.append(input())

for _ in range(m):
    no_hear.append(input())

set(no_see)
set(no_hear)

if len(no_see) < len(no_hear):
    longer = no_hear
    shorter = no_see
else:
    longer = no_see
    shorter = no_hear

result = []
for i in shorter:
    if i in longer:
        result.append(i)

print(len(result))

for i in range(len(result)):
    print(result[i])
"""
import sys

n,m = map(int,sys.stdin.readline().split())

no_see = [sys.stdin.readline().strip() for _ in range(n)]

no_hear = [sys.stdin.readline().strip() for _ in range(m)]

result = list(set(no_hear)&set(no_see)) # set 과 &를 이용해서 겹치는 이름을 찾는다.

result.sort() # 사전순으로 나열

print(len(result))

for i in result:
    print(i)