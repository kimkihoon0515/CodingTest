n = int(input()) # n번째 피보나치 수를 입력받는다.

fib = [] # 피보나치 배열을 만든다.
for i in range(n+1):
    if i == 0:
        fib.append(0) # 0이면 0을 추가하고
    elif i == 1:
        fib.append(1) # 1이면 1을 추가한다
    else:
        fib.append(fib[i-2]+fib[i-1]) # 그 다음부터는 i-2와 i-1값의 합을 구함으로써 피보나치 배열을 추가해 나간다.
print(fib[n]) 

