import sys

n,m = map(int,sys.stdin.readline().split()) # 기타줄 n개 브랜드 m개

guitar = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

six_guitar = sorted(guitar,key=lambda x:x[0])
one_guitar = sorted(guitar,key=lambda x:x[1])


answer = 0

import math

if one_guitar[0][1]*6 <six_guitar[0][0]:
    answer += one_guitar[0][1]*n
else:
    if n >= 6:
        if n/6 !=0:
            if six_guitar[0][0]* math.ceil(n/6) < six_guitar[0][0]*(n//6)+one_guitar[0][1]*(n%6):
                answer += six_guitar[0][0]*math.ceil(n/6)
            else:
                answer += six_guitar[0][0]*(n//6)+one_guitar[0][1]*(n%6)
        else:
            answer += six_guitar[0][0]*(n//6)
    else:
        if six_guitar[0][0]*math.ceil(n/6) < six_guitar[0][0]*(n//6)+one_guitar[0][1]*(n%6):
            answer += six_guitar[0][0]*math.ceil(n/6)
        else:
            answer += six_guitar[0][0]*(n//6)+one_guitar[0][1]*(n%6)

print(answer)