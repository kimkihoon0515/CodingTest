import sys

n = int(sys.stdin.readline())

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,num):
        if num%i== 0:
            return False
    return True

def dfs(answer):
    if len(str(answer)) == n:
        print(answer)
    else:
        for i in range(10):
            ans = answer * 10 + i # 늘린 자리수
            if prime(ans):
                dfs(ans)

prime_num = [2,3,5,7]

for i in prime_num:
    dfs(i)
    
    