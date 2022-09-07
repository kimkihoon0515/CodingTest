from codecs import IncrementalDecoder
from re import I
import sys

li = [64,32,16,8,4,2,1]

x = int(sys.stdin.readline())

if x in li:
    print(1)

else:
    cnt = 0
    for i in li:
        if x == 0:
            break
        if i<=x:
            x-= i 
            cnt +=1
    print(cnt)