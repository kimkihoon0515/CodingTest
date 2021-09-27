""" 런타임 에러 오류 코드
n = int(input())

def fib(n):
    if n == 2:
        return 2
    if n == 3:
        return 3
    else:
        return (fib(n-1)+fib(n-2)) %  15746
    
print(fib(n))
"""

n = int(input())

list = [1,2]

for i in range(2,n):
    list.append((list[i-1]+list[i-2])%15746)

print(list[n-14])