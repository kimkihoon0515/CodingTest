a = ' '+input() # 첫 번째 배열을 입력받는다.
b = ' '+input() # 두 번째 배열을 입력받는다.

result = [[0] * len(b) for _ in range(len(a))] # LCS를 판별하는 배열을 0으로 초기화해서 만든다.
for i in range(1, len(a)): # 1부터 반복문을 돌린다. 0은 생각할 필요가없기때문
    for j in range(1, len(b)): 
        if a[i] == b[j]: # 만약 같은 문자를 발견하면 왼쪽 대각선보다 1증가한상태로 저장한다.
            result[i][j] = result[i - 1][j - 1] + 1 
        else: # 그렇지 않으면 행의 최대값을 저장해놓는다.
            result[i][j] = max(result[i - 1][j], result[i][j - 1])


print(max(max(result))) # 최대값 출력