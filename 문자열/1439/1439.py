import sys

s = sys.stdin.readline().strip()    

zero = s.split('1') # 1을 기준으로 분리
one = s.split('0') # 0을 기준으로 분리

a = len(zero) - zero.count('') # 배열에서 '' 개수 제거
b = len(one) - one.count('') 

print(min(a,b)) # 둘 중 작은거 출력