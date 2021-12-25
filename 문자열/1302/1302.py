import sys
from collections import Counter

n = int(sys.stdin.readline().strip())

name = sorted(list(sys.stdin.readline().strip() for _ in range(n))) # 사전순으로 출력하기위해 정렬

book = Counter(name) # dict 형태로 변환

answer = [k for k,v in book.items() if v == max(book.values())] # 가장 값이 큰 것을 출력

print(answer[0])