""" 왜인지 모르겠지만 최소길이 2개를 비교해서 LCS배열을 찾고 그 배열을 이용해서 가장 긴 수열과 LCS를 찾으면 틀린다.
import sys

first = sys.stdin.readline().strip().upper()
second = sys.stdin.readline().strip().upper()
third = sys.stdin.readline().strip().upper()

if len(first) == min(len(first),len(second),len(third)):
    a = first
    if len(second) == min(len(second),len(third)):
        b,c = second,third
    else:
        c,b = second,third
elif len(second) == min(len(first),len(second),len(third)):
    a = second
    if len(first) == min(len(first),len(third)):
        b,c = first,third
    else:
        c,b = first,third
elif len(third) == min(len(first),len(second),len(third)):
    a = third
    if len(second) == min(len(first),len(second)):
        b,c = second,first
    else:
        c,b = second,first
            
result = [0]
for i in range(1,len(a)+1):
    for j in range(i,len(b)+1):
        if a[i-1] in b:
            result.append(a[i-1])
            break

matrix = [[0 for _ in range(len(result)+1)] for _ in range(len(third)+1)]

for i in range(1,len(third)+1):
    for j in range(1,len(result)+1):
        if third[i-1] == result[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

print(matrix[-1][-1])
""" 
import sys # 3중 LCS를 구한다.

s = [sys.stdin.readline().strip() for i in range(3)]
matrix = [[[0 for i in range(len(s[0]) + 1)] for j in range(len(s[1]) + 1)] for k in range(len(s[2]) + 1)]


for k in range(1,len(s[2])+1):
    for j in range(1,len(s[1])+1):
        for i in range(1,len(s[0])+1):
            if s[0][i-1] == s[1][j-1] == s[2][k-1]:
                matrix[k][j][i] = matrix[k-1][j-1][i-1] + 1
            else:
                matrix[k][j][i] = max(matrix[k-1][j][i],matrix[k][j-1][i],matrix[k][j][i-1],matrix[k-1][j-1][i],matrix[k][j-1][i-1],matrix[k-1][j][i-1])
                
print(matrix[-1][-1][-1])
