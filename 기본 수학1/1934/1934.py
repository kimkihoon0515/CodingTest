import sys
import math

t = int(sys.stdin.readline())

def lcm(a,b):
    gcd = math.gcd(a,b) # 최대공약수
    return int((a/gcd)*(b/gcd)*gcd) # 최소공배수

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(lcm(a,b))