n = int(input()) # n개의 부등호의 개수를 입력받고 math라는 배열에 넣는다.

math=list(map(str,input().split()))

check=[False] * 10 # dfs를 사용하기 위한 배열

mx = "" # 최대값
mn = "" # 최소값

def is_true(i,j,k): # 가능과 불가능을 판별하는 함수
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def solve(index,s): # dfs를 정의한다.
    
    global mn,mx 
    if index == n+1:
        if not len(mn): # mn에 값이 없으면 mn 최소값 s를 넣고 mx에 값이 없으면 최대값 s를 넣는다.
            mn = s
        else:
            mx = s
        return
    for i in range(10): # 0 ~ 9까지중복이 안되어있으면 
        if not check[i]:
            if index == 0 or is_true(s[-1],str(i),math[index-1]): #조건에 맞지 않으면 dfs를 다시 시작한다.
                check[i] = True
                solve(index+1,s+str(i)) 
                check[i] = False
solve(0,"")
print(mx)
print(mn)            