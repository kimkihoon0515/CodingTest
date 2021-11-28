import sys

t = int(sys.stdin.readline())

def call(phone):
    answer = []
    phone.sort() 
    for i in range(len(phone)-1):
        if phone[i] in phone[i+1][0:len(phone[i])]: # 접두사만 비교하면 된다.
            answer.append(-1)
        else:
            answer.append(1)
    return answer

for _ in range(t):
    n = int(sys.stdin.readline())
    phone = [sys.stdin.readline().strip() for _ in range(n)]
    if -1 in call(phone):
        print('NO')
    else:
        print('YES')