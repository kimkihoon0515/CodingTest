# 도저히 모르겠음... 어떻게 이런 생각을 하는지 잘 모르겠다.
def solution(N, number):
    answer = -1
    dp = [[] for _ in range(9)] # 0~8까지만 구하면 됨
    for i in range(1,9):
        dp[i].append(int(str(N)*i))
        for j in range(1,i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].append(k+l)
                    dp[i].append(k-l)
                    dp[i].append(k*l)
                    if l!=0:
                        dp[i].append(k//l)
        dp[i] = list(set(dp[i]))
        if number in dp[i]:
            return i
    return answer