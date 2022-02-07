import sys
from collections import Counter

n = int(sys.stdin.readline())

card = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

dic = dict(Counter(card))
dic = sorted(dic.items(), key=lambda x: (-x[1],x[0]))
print(dic[0][0])