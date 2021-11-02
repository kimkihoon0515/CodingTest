"""
meet in the middle 알고리즘을 사용해야 시간복잡도를 줄일 수 있음.
전체를 2개의 그룹으로 나눈다.
그 그룹으로 나누고 브루트 포스 함수를 통해서 그룹에서 나올 수 있는 모든 경우의 수를 구한다.
"""
import sys

n,c = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
a = li[:n//2]
b = li[n//2:]
a_result = []
b_result = []

def brute(index,w,li,size,result): # a와b로 나누어서 합들을 그 결과배열에 저장한다. 
    if index >= size:
        result.append(w)
        return
    brute(index+1,w,li,size,result)
    brute(index+1,w+li[index],li,size,result)

def bin(start,end,target,arr): # binary search로 b의 합을 돌려준다.
    while start <end:
        mid = (start+end)//2
        if arr[mid] <=target:
            start = mid + 1
        else:
            end = mid
    return end

brute(0,0,a,len(a),a_result)
brute(0,0,b,len(b),b_result)

b_result.sort()
cnt = 0

for i in a_result: # a 합중에서 c-i보다 작거나 같은 수들 중에 가장 큰 값을 b 합에서 찾아서 세어준다.
    if c<i:
        continue
    else: # 이것들은 전부 가방에 넣을 수 있기 때문.
        cnt += bin(0,len(b_result),c-i,b_result)
print(cnt)