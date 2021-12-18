import sys

def search(start,end,target): # 이진탐색 알고리즘
    while start <= end: 
        mid = (start+end)//2
        if a[mid] == target: # a 배열안에 들어있으면
            return 1 # 1 반환
        elif a[mid]< target: # 만약 중앙값이 target보다 작으면
            start = mid + 1 # start 조정
        else: # 중앙값이 target보다 크면
            end = mid -1 # end 조정
    return 0 # a배열안에 값이 없으면 0 반환

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    b = list(map(int,sys.stdin.readline().split()))
    a.sort() # 이진탐색을 위해 sort해놓는다.
    
    for i in b: # b 의 원소들을 하나씩 반복문돌려서 확인
        print(search(0,n-1,i))