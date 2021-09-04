import math
a, b, v = map(int,input().split()) # 3개의 숫자를 입력받는다.

date = math.ceil((v-a)/(a-b)) +1
print(date)