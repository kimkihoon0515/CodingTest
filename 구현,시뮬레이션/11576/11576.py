import sys

a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))   

answer = 0

ans = []
for i in range(m):
    answer += num[-1]* (a**i) # 입력받은 숫자를 10진수로 바꾼다.
    num.pop(-1)

while answer !=0:
    ans.append(str(answer % b)) # y진수로 바꾸는 과정
    answer = answer // b
    
print(' '.join(ans[::-1]))
