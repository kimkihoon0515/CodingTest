import sys
n = int(sys.stdin.readline().strip())

def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

answer = 0

for i in range(n,1005001): # 범위 조정해줘야함 1000001로 하면 틀림
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if prime(i):
          answer = i
          break

print(answer)  

