a = list(input().rstrip()) # 첫 번째 배열을 입력받는다.
b = list(input().rstrip()) # 두 번째 배열을 입력받는다.
#print(a)
#print(b)
ans = []
result = [[""] * (len(b)+1)  for _ in range(len(a)+1)] # LCS를 판별하는 배열을 ""으로 초기화해서 만든다.

for i in range(1, len(a)+1): # 1부터 반복문을 돌린다. 0은 생각할 필요가없기때문
    for j in range(1, len(b)+1): 
        if a[i-1] == b[j-1]: # a와b의 i,j번째 문자가 일치한다면 대각선의 result + 그 문자 를 새로운 result 에 저장.
            result[i][j] = result[i - 1][j - 1] + a[i-1]
        else: # 그렇지 않을경우
            if len(result[i-1][j]) >= len(result[i][j-1]): # 둘 중 길이가 긴 것을 새로운 result에 대입한다.
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = result[i][j-1]


if len(result[-1][-1]) == 0:
    print(0)
else:
    print(len(result[-1][-1]))
    print(result[-1][-1])



