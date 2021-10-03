import sys
k = int(sys.stdin.readline()) # 숫자의 개수를 입력받는다.

li = [] # 숫자들을 넣을 배열과 누적합을 선언한다.
sum = 0
for _ in range(k): 
    num = int(sys.stdin.readline())
    if num == 0: # 만약 0을 입력받으면 누적합에서 배열의 가장 마지막 원소를 지우고 배열에서도 지운다.
        sum -= li[len(li)-1]
        li.pop()
    else: # 그렇지 않으면 누적합에 입력값들을 계속 합해나간다.
        li.append(num)
        sum += num
print(sum)