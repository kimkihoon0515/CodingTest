import math # ceil 함수 쓰기위해
a, b, v = map(int,input().split()) # 3개의 숫자를 입력받는다.

date = math.ceil((v-a)/(a-b)) +1 # ceil : 소수점 올림.
print(date)