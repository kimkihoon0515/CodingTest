import sys

# 확장자 별로 정리
# 사전 순 정렬

n = int(sys.stdin.readline())

files = list(sys.stdin.readline().strip() for _ in range(n))

dic = {}

for i in range(len(files)):
    name,typ = files[i].split('.')
    if typ not in dic:
        dic[typ] = 1
    else:
        dic[typ] += 1

ans = []

for key,value in dic.items():
    ans.append([key,value])

ans.sort()

for i in range(len(ans)):
    a,b = ans[i]
    print(a,b)