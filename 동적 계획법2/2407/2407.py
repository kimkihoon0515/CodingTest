import sys
import math

n,m = map(int,sys.stdin.readline().split())

result = 1
for i in range(m):
    result *= (n-i)

print(result // math.factorial(m))

