import sys

e,s,m = map(int,sys.stdin.readline().split()) # e: 지구, s: 태양, m: 달

result = 1

while True:
    if (result - e) % 15 == 0 and (result - s) % 28 == 0 and (result - m) % 19 == 0:
        break
    else:
        result += 1
print(result)
