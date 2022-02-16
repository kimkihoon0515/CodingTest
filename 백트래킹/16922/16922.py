import sys
from itertools import combinations_with_replacement

n = int(sys.stdin.readline())

num = [1,5,10,50]

ans = []

for number in combinations_with_replacement(range(4),n): # 중복을 제거하고 4개중에 n개를 고름
    # 1,1 1,5 1,10, 1,50 이런식으로
    sum = 0
    for i in number:
        sum += num[i]  # 고른 n개의 수를 합치고
    if sum not in ans: # 중복이되지않게 넣는다.
        ans.append(sum)
    
print(len(ans))
