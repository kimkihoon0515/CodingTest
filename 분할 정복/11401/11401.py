import sys
n,k = map(int,sys.stdin.readline().split())

p = 1000000007

def solve(a,b): # 페르마의 소정리를 이용해서 풀어야하는데 너무 어렵다.
    if b == 0:
        return 1
    if b % 2 == 0:
        return (solve(a,b//2) ** 2) % p
    else:
        return(solve(a,b//2) ** 2 * a) % p

fact = [ 1 for i in range(n+1)]

for i in range(2,n+1):
    fact[i]= fact[i-1] * i % p

a = fact[n]
b = (fact[n-k] * fact[k]) % p


print((a % p) * (solve(b,p-2)%p) %p)

