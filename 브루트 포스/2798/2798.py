from itertools import combinations
n,m = map(int,input().split()) # 카드의 개수 n과 그 카드들 중 3장의 합이 될 m을 입력받는다.

card = list(map(int,input().split())) # 카드의 개수만큼 입력을 받는다.

max = 0 # 카드 3개 합의 최대값

for i in combinations(card,3): # python 라이브러리 combination을 활용한다.
    three_sum = sum(i) # 임의로 3개가 선정된 것들의 합
    if max < three_sum <= m: 
        max = three_sum
print(max)