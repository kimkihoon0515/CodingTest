import sys

a = int(sys.stdin.readline())

money = 1000 - a

en = [500,100,50,10,5,1]

sum = 0
for i in en:
    sum += money // i
    money %= i
print(sum)