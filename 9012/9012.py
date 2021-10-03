import sys
t = int(sys.stdin.readline()) # 테스트 케이스의 개수를 입력받는다.

for i in range(t): 
    s = list(sys.stdin.readline()) # 배열에 문자열을 넣고 () 중에서 ( 가먼저 나와야 하므로 (가 나올때마다 sum을 하나씩 올려주고 아니면 하나씩 내려준다.
    sum = 0
    for i in range(len(s)-1):
        if s[i] == '(':
            sum +=1
        else:
            sum -=1
    if sum < 0: # 만약 ( 보다 ) 가 많을 경우엔 안되는 경우이다.
            print('NO')
            break
    if sum == 0: # 합이 0이되면 vps인 경우
        print('YES')
    elif sum > 0: # 합이 0보다 크면 안되는 경우이다.
        print('NO')