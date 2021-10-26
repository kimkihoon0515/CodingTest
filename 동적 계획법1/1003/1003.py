""" 시간초과
n = int(input()) # 출력하고자하는 테스트케이스의 개수를 입력받는다.

zero_count = 0
one_count = 0

def fib(index):
    global zero_count, one_count
    if index == 0:
        zero_count+=1
        return 0
    if index == 1:
        one_count+=1
        return 1
    else:
        return fib(index-1)+fib(index-2)

for i in range(n):
    a = int(input())
    fib(a)
    print(zero_count,one_count)
"""

t = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(n) : #[0,1,3]
    if len(zero) <= n :
        for i in range(len(zero), n+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(t) : #[3]
    a = int(input()) #[0,1,3]
    fibo(a)