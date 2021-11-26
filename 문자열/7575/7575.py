import sys

n,k = map(int,sys.stdin.readline().split())

m = []
for _ in range(n):
    a = int(sys.stdin.readline())
    m.append(list(map(int,sys.stdin.readline().split())))

def makeTable(tmp):
    table = [0] * k
    i = 0 
    for j in range(1,k):
        while i > 0 and tmp[i]!=tmp[j]: 
            i = table[i-1]
        if tmp[i] == tmp[j]:
            i += 1
            table[j] = i
    return table

def kmp(s,f,tmp):
    i = 0 # i를 통해 table 값을 갱신시킨다.
    for j in range(len(s)): 
        while i > 0 and s[j] != f[i]: # i와 j를 비교해서 다르면
            i = tmp[i-1] # 다르게 나온 곳-1번째 table 인덱스로 다시 되돌아가서 다시 비교한다.
        if s[j] == f[i]: # 모든 문자열이 전부 일치하면
            if i == k-1: # i가 패턴의 길이보다 하나 작으면 
                return 1 # 패턴을 찾은 것이므로 1을 반환
            else:
                i += 1 # 모든 문자열이 전부 일치하지 않으면 i를 하나씩 늘려서 비교한다.
    return 0 # 패턴을 못찾은 경우 0을 반환


for i in range(len(m[0])-k+1): # 코드의 길이는 접두사부분까지만 돌리면 되므로 0 부터 패턴의 길이만큼 뺀것+1을 돌리면 된다. 
    t = makeTable(m[0][i:i+k]) # k개의 길이만큼 코드가 같아야 하므로 그것을 패턴으로 makeTable 한다.
    for j in range(1,n): # 프로그램의 개수가 3개 이므로
        c = kmp(m[j],m[0][i:i+k],t) # kmp를 통해 비교해서 k개 이상 겹치는 코드가 존재하는지 판단
        if not c: # 코드가 존재하지 않으면
            c = kmp(m[j][::-1],m[0][i:i+k],t) # 뒤집어서도 비교해본다.
        if not c: # 만약 그래도 존재하지 않으면
            break # 반복문을 탈출하여 No 출력
        if j==n-1: # 만약 바이러스임을 감지하면 Yes 출력
            print('YES')
            exit(0) # 그대로 프로그램 종료
print('NO')