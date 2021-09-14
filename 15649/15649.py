# backtracking : 
# 1. DFS를 진행한다.
# 2. 노드의 유망성을 점검한 후 nonpromising(해답이 나올 가능성 없는 것) 이면 부모노드로 backtracking하고 -promising(해답 나올 가능성은 있는것)한 다른 자식 노드로 검색을 진행

n,m = map(int,input().split()) # n,m을 입력받는다.

arr=[False] * n # 체크 여부

result=[] # 결과물

def dfs(depth,n,m): 
    if depth == m: # 탈출 하는 조건
        print(' '.join(map(str,result))) # list 를 str 으로 합쳐서 출력한다. 
        return
    for i in range(len(arr)): # 체크범위 설정
        if not arr[i]: # 체크 안했다면
            arr[i] = True # 중복을 제거
            result.append(i+1) # 결과 배열에 숫자 입력
            dfs(depth+1,n,m) # 재귀호출로 다시 탐색
            arr[i] = False # 체크 완료
            result.pop() # 체크 내용 제거          
dfs(0,n,m)