from itertools import permutations
n = int(input()) # n개의 정수를 입력받는다.

list = list(map(int,input().split())) # n개의 정수를 list에 넣는다.

per = permutations(list) # permutation을 이용해서 list를 새로 만든다.
answer = 0 # 결과값중 최대값을 저장하는 변수

for i in per: # 조합들을 차례로 반복문을 돌린다.
    sum = 0 # 각 조합별 i와 i+1의 차이를 구하는 변수
    for j in range(len(i)-1): # 차이를 구해서 그 차이가 결과값보다 크면 결과값에 sum을 복사한다.
        sum += abs(i[j]-i[j+1])
    if sum > answer:
        answer = sum

print(answer)