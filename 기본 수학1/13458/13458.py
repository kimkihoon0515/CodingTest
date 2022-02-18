import sys

n = int(sys.stdin.readline()) # n개 시험장
a = list(map(int,sys.stdin.readline().split())) # 각 시험장 응시자 수
b,c = map(int,sys.stdin.readline().split()) # 총감독은 b명, 부감독관은 c명 감시 가능

num = []
for i in a:
    num.append(i-b)
for i in range(n):
    if num[i]> 0: # 0 보다 크면
        if num[i] % c == 0: # c로 나눴을 때 0인경우
            num[i] = num[i] // c 
        else:
            num[i] = num[i] // c + 1
    else: # 음수가 나오는 경우
        num[i] = 0
        continue
print(n+sum(num))
