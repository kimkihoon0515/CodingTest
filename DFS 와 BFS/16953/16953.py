import sys

a,b = map(int,sys.stdin.readline().split()) # 2 → 4 → 8 → 81 → 162, 100 → 200 → 2001 → 4002 → 40021
result = 1

while True:
    if a == b:
        break
    elif a > b: # a가 더 커지면 -1 출력
        result = -1
        break
    elif b % 10 == 1: # 10으로 나눠서 1이 남으면 결과값 +1
        result += 1
        b //= 10
    elif b % 2 == 0: # 2로 나누어떨어지면 결과값 +1
        b //=2
        result +=1
    else: # 둘다 안되면 -1 출력
        result = -1
        break
print(result)