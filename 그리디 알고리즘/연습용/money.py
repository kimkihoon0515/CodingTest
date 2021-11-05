import sys
# 시간복잡도는 O(n)
n = 1260
cnt = 0
li = [500,100,50,10]

for i in li:
    cnt += n // i
    n %= i
print(cnt)