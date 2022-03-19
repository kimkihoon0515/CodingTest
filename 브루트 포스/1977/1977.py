import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())


sum = 0
answer = 0
for i in range(m,n+1):
    if str(math.sqrt(i))[-1] == '0' and sum == 0:
        answer = i
        sum += i
    elif str(math.sqrt(i))[-1] == '0':
        sum += i
        

if sum == 0:
    sum = -1
print(sum)
if answer != 0:
    print(answer)