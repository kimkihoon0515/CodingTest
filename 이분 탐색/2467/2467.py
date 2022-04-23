import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

left = 0
right = n-1
minimum = sys.maxsize

ans = []

while left<right:
    answer = li[left]+li[right]
    
    if abs(answer) < minimum:
        ans.append([left,right]) # 인덱스 저장
        minimum = abs(answer)
    if answer > 0: # 0보다크면 오른쪽에서
        right -=1
    elif answer < 0: # 0보다작으면 왼쪽에서
        left +=1
    else: # 같으면 종료
        break
print(li[ans[-1][0]],li[ans[-1][1]]) # 저장된 인덱스들 중 가장 적은 차이가 날수록 나중에 저장되므로