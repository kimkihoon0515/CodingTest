import sys
n = int(sys.stdin.readline()) # 배열의 길이를 입력받는다.
li = [] # 작은 수 부터 차례대로 배열에 넣는다.
result = [] # +,-를 저장할 배열
cnt = 1 # 1~n까지의 숫자를 차례로 하나씩 증가시켜서 push하기 위한 변수
flag = 0 # 조건에 맞지 않으면 NO를 출력하기 위한 변수
for _ in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num: # 1~n까지 반복해서 li 배열에 push 하고 push 할 떄마다 +를 결과 배열에 넣는다.
        li.append(cnt)
        result.append('+')
        cnt+=1
    if li[-1] == num: # li의 가장 마지막 원소가 내가 지금 입력한 숫자와 같아지면 그 원소를 순차적으로 입력되던 배열에서 빼고 결과배열에 -를 넣는다.
        li.pop()
        result.append('-')
    else: # 입력한 배열을 조합으로 못만들 경우에는 no를 출력한다. 
        flag = 1
if flag == 1:
    print('NO')
else:
    for i in result:
        print(i)
