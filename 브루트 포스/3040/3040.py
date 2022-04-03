import sys
from itertools import combinations

nums = list(int(sys.stdin.readline().strip()) for _ in range(9))

li = list(combinations(nums,7))

for i in li:
    if sum(i) == 100:
        for j in i:
            print(j)