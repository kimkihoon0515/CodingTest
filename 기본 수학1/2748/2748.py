import sys

n = int(sys.stdin.readline())

fib = []

ans = 0

for i in range(n+1):
    if i ==0:
        ans = 0
    elif i <= 2:
        ans = 1
        
    else:
        ans = fib[-1]+ fib[-2]
    fib.append(ans)
print(fib[-1])