import sys

n = int(sys.stdin.readline())

li = [list(map(lambda x: ord(x)-65,sys.stdin.readline().strip())) for _ in range(n)] # 알파벳을 아스키 코드 숫자 -65로 곱하기 편하기 바꿔준다.
alphabet = [0 for _ in range(26)]

for i in range(n):
    j = 0
    for k in li[i][::-1]: # 중요도를 계산하는 것. 자리수를 계산한다. 
        alphabet[k] += (10**j) # A가 10의 자리 수이면 10, 100의 자리 수이면 100 이런식으로 알파벳의 중요도를 갱산힌다.
        j+=1    

alphabet.sort(reverse=True) # 역정렬

ans,t = 0,9 # 결과값과, 0 ~ 9까지 숫자 대입용 변수
for i in range(26): # 알파벳 길이만큼
    if alphabet[i] == 0: # 알파벳에 숫자를 모두 대입했다면 반복문 종료
        break
    ans += (t*alphabet[i]) # 결과값에 알파벳의 중요도 * 대입한 숫자를 더해서 갱신해간다.
    t -= 1 # 중요도가 낮아질 수록 대입될 숫자는 줄어든다.
print(ans)
