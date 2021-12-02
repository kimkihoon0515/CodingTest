import sys

n = sys.stdin.readline().strip()
length = len(n) - 1
cnt = 0
i = 0
while i < length:
    cnt += 9 * (10 ** i) * (i + 1) # 1의 자리수들 전부 합한 자리수 = 9, 10의 자리수 전부 합한 것: 90*2, 100의 자리수 전부 합한 것: 900*3
    i += 1 # 10의 자리수를 더해간다.
cnt += ((int(n) - (10 ** length)) + 1) * (length + 1) # 값을 전부 합해서 출력
print(cnt)