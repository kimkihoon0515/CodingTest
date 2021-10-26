dp = [[[0] * 21 for _ in range(21)] for _ in range(21)] # dp 결과값을 받을 이중배열을 선언해준다.


def w(a,b,c): # 문제에 나온 것들을 조건문으로 해서 조건에 맞게 저장한다.
    if a<=0 or b <=0 or c <=0: 
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if dp[a][b][c]: # dp값이 있으면 그대로 출력
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return dp[a][b][c]


while True: # -1 -1 -1 을 입력으로 받기 전까지 조건에 맞게 출력한다.
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')