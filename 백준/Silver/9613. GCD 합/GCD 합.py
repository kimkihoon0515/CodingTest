import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    li = list(map(int,sys.stdin.readline().split()))
    ans = 0
    for i in range(1,len(li)):
        for j in range(i+1,len(li)):
            ans += math.gcd(li[i],li[j])
    print(ans)