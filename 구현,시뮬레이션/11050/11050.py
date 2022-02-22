from itertools import combinations
import sys

n,k = map(int,sys.stdin.readline().split())

print(len(list(combinations(range(n),k))))