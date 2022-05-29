import sys
from itertools import product

n,m = map(int,sys.stdin.readline().split())

li = sorted(list(map(int,sys.stdin.readline().split())))

for i in product(li,repeat=m):
    print(*i)