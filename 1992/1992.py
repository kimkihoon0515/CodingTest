import sys

n = int(sys.stdin.readline())

li = [list(map(int,input()))for _ in range(n)]

def cut(x,y,n):
    if n == 1: # 1개의 칸만 비교할 경우 
        return str(li[x][y]) 
    result = []
    check = li[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n): 
            if check !=li[i][j]: # 색이다르면 
                result.append('(') # 조건에맞게 출력형식을 정하고 결과 배열에 그 결과를 넣고 다시 재귀함수를 호출한다.
                result.extend(cut(x,y,n//2))
                result.extend(cut(x,y+n//2,n//2))
                result.extend(cut(x+n//2,y,n//2))
                result.extend(cut(x+n//2,y+n//2,n//2))
                result.append(')')
                return result
    return str(li[x][y])

print(''.join(cut(0,0,n)))


