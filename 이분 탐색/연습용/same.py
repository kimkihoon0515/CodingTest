import sys
import bisect

n,x = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

left_value = bisect.bisect_left(li,x)
right_value = bisect.bisect_right(li,x)

cnt = right_value - left_value

print(cnt if cnt !=0 else -1)
