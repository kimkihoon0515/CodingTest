""" 시간초과 발생 
import sys
tree = []
cnt = 0

while True:
    name = sys.stdin.readline().strip()
    if name == '':
        break
    tree.append(name)
    cnt += 1

li = set(sorted(tree))

result = []
for i in li:
    numcnt = tree.count(i)
    result.append([i,numcnt])
result.sort()

for i in range(len(result)):
    print('%s %.4f' % (result[i][0],result[i][1] * 100 /cnt))
"""
import sys
from typing import DefaultDict

tree = DefaultDict(int) # 개별적 나무의 개수 (시간초과발생방지용)
cnt = 0 # 나무의 총 개수
while True:
    name = sys.stdin.readline().strip()
    if name == '':
        break
    tree[name] += 1
    cnt +=1

result = list(tree.keys()) # 나무의 이름만 추출한다. 
result.sort() # 이름순으로 정렬
#print(result)
for i in result:
    print('%s %.4f' % (i,tree[i]*100/cnt))