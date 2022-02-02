import sys

i = 1
while True:
    l,p,v = map(int,sys.stdin.readline().split())
    if l == p == v == 0:
        break
    a = (v//p)*l
    b = min(v%p,l)
    answer = a+b
    print('Case %d: %d'%(i,answer))
    i+=1