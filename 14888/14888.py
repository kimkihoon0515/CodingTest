N = int(input()) # 입력값을 받는다.
nums = list(map(int, input().split())) # 숫자들을 입력받는다.
add, sub, mul, div = map(int, input().split()) # 사칙연산의 개수를 입력받는다.

min_, max_ = 1000000000,-1000000000 # 최대와 최소값을 정한다.

def dfs(i, res, add, sub, mul, div): # dfs 구조
    global max_, min_ 
    if i == N: # n번째 계산값이면 최대값과 최소값을 return한다.
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)
