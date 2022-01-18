import sys,math

s = sys.stdin.readline().strip().split(':')
a = int(s[0])
b = int(s[1])

gcd = math.gcd(a,b)
a = a//gcd
b = b//gcd
print(str(a)+':'+str(b))
