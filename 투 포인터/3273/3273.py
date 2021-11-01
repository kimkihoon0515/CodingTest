"""
투 포인터 알고리즘을 사용해서 해결하는 문제이다. 투 포인터 알고리즘은 리스트가 정렬되어있을 경우 O(n) 아닐경우 O(nlogn)
의 시간복잡도를 가지기 때문에 이중for문 보다 빠르다.

"""
import sys

n = int(sys.stdin.readline())

li = sorted(list(map(int,input().split())))

x = int(sys.stdin.readline())

cnt = 0
left = 0 # 시작지점
right = n-1 # 끝 지점

while left < right: # 시작지점이 끝지점
    sum = li[left]+li[right]
    if sum > x:
        right -=1
    elif sum <x:
        left +=1
    else:
        cnt+=1
        left+=1
        right-=1
print(cnt)