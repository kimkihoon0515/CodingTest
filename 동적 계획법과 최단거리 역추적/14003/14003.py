import sys
from bisect import bisect_left

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

queue = [] # 차례대로 증가하는 배열을 만들기 위한 배열
tmp = [] # (위치,값) 의 배열

for i in li:
    if not queue or i > queue[-1]:  # queue 에 없거나 queue에서 가장 큰 수보다 큰 값이면 
        queue.append(i) # queue에 그것을 넣는다.
        tmp.append((len(queue)-1,i)) # tmp 배열에 (위치,값) 을 넣는다.
    else: # 그렇지 않다면 즉 작거나 같다면
        queue[bisect_left(queue,i)] = i # 이진탐색으로 i값이 어디에 있는 값인지 찾고 
        tmp.append((bisect_left(queue,i),i)) # tmp 배열에 그 값이 무엇인지 어디에있는 값인지 그것을 복사해서 넣는다. 

ans = [] # 결과 배열
end = len(queue) -1 # queue 의 마지막 원소의 위치

for i in range(len(tmp)-1,-1,-1): # tmp 배열에서 값 만 찾아서 ans 배열에 넣는다.
    if tmp[i][0] == end: # 거꾸로 들어간다. 
        ans.append(tmp[i][1])
        end -=1
# ans 배열에 큰 수대로 들어갔으므로 reverse를 통해 뒤집어서 출력해줘야한다.
print(len(ans)) # 길이를 출력하고
print(*reversed(ans)) # 값들을 뒤집어서 출력해준다.
