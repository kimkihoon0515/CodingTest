import sys
import heapq

n = int(sys.stdin.readline())
leftheap=[]
rightheap=[]
for _ in range(n):
    x = int(sys.stdin.readline())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap,-x) # 왼쪽heap은 최대로 정렬해놓고 
        #print('leftheap: ',leftheap)
    else:
        heapq.heappush(rightheap,x) # 오른쪽heap은 최소로 정렬하면 왼쪽이 항상 중앙값이 된다. 
        #print('rightheap: ',rightheap)

    if len(leftheap) != 0 and len(rightheap) !=0 and leftheap[0] *-1 > rightheap[0]:
        heapq.heappush(leftheap,heapq.heappop(rightheap) * -1) # 왼쪽 heap의 첫번째 요소는 오른쪽heap에서 가장 큰 값
        heapq.heappush(rightheap,heapq.heappop(leftheap)*-1) # 오른쪽 heap에서 첫번째 요소는 왼쪽heap에서 가장 작은 값
    print(leftheap[0] * -1) # 그러므로 왼쪽 heap의 첫 번째 요소가 오른쪽 첫 번째 요소보다 크면 왼쪽과 오른쪽을 서로 바꿔준다. 그리고 왼쪽의 첫번째 원소를 출력한다.(-1)을 곱해서 양수로 출력.
