import sys


n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().split()))


def binary(start,end,target):
    while start < end:
        mid = (start+end) // 2
        
        if ans[mid]< target: # target보다 작으면 start를 증가시킨다.
            start = mid + 1
        else:
            end = mid 
    return end

ans = []

for i in a:
    if not ans:
        ans.append(i) # 맨 처음원소를 넣는다.
        continue 
    if ans[-1] < i : # ans의 맨 앞의 원소가 i보다 작으면 i를 넣는다.
        ans.append(i)
    else:
        index = binary(0,len(ans)-1,i) 
        ans[index] = i

print(len(ans))