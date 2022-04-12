''' 시간초과 오류가 계속남 ㅠ
import sys

# 각 남자는 모두 여자와 춤출수 있고
# 여자는 남자와 춤출수 있다.
# 남자 선호 유형 : 자기보다 키큰 여자, 키 작은 여자
# 여자 선호 유형 : 키큰남자 키작은 남자

n = int(sys.stdin.readline().strip())
man = list(map(int,sys.stdin.readline().split())) # 키가 양수이면 키큰 여성 선호 음수이면 키작은 여성 선호
woman = list(map(int,sys.stdin.readline().split()))


man1 = sorted([i for i in man if i > 0])
man2 = sorted([i for i in man if i <0],reverse=True)
woman1 = sorted([i for i in woman if i > 0])
woman2 = sorted([i for i in woman if i <0],reverse=True)

cnt = 0
for i in range(len(man1)):
    for j in range(len(woman2)):
        if man1[i] + woman2[j] <0:
            cnt +=1
            woman2.pop(j)
            break

for i in range(len(woman1)):
    for j in range(len(man2)):
        if woman1[i] + man2[j] < 0:
            cnt+=1
            man2.pop(j)
            break
            
print(cnt)   
'''
# 정답코드
import sys
N = int(sys.stdin.readline())
man = list(map(int, sys.stdin.readline().split()))
woman = list(map(int,sys.stdin.readline().split()))

m_plus = sorted([i for i in man if i > 0])
m_minus = sorted([i for i in man if i < 0], reverse=True)
w_plus = sorted([i for i in woman if i > 0])
w_minus = sorted([i for i in woman if i < 0], reverse=True)

def calForResult(plus, minus):
    i,j = 0,0
    cnt = 0
    while i < len(plus):
        while j < len(minus):
            if plus[i] + minus[j] < 0 :
                j += 1
                cnt += 1
                break
            else :
                j += 1
        if j == len(minus) :
            break
        i += 1
    return cnt

cnt = calForResult(m_plus,w_minus)
cnt += calForResult(w_plus,m_minus)
print(cnt)