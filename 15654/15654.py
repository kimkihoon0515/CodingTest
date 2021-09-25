n,m = map(int,input().split()) # n,m 을 입력받는다.

list = sorted(map(int,input().split())) # 숫자들을 입력받아서 배열에 정렬하여 저장한다.

visited = [False] * n # 탐색 확인용 배열
out = [] # 출력용 배열

def dfs(depth,n,m): # dfs 알고리즘 구조 
    if depth == m: # m개의 숫자길이가 되면 형식에 맞게 출력한다.
        print(' '.join(map(str,out)))
        return
    for i in range(n): # 배열의 길이가 m개가 아니면 n번만큼 반복문을 돌린다.
        if not visited[i]: # 아직 탐색을 하지 않았다면
            visited[i] = True # 탐색을 했다고 표시하고 list[i]를 출력용 배열에 입력한다.
            out.append(list[i])
            dfs(depth+1,n,m) # 재귀 방식으로 다시 호출한다.
            out.pop() 
            visited[i] = False
dfs(0,n,m)