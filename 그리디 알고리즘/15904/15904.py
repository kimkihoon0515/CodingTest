import sys

s = sys.stdin.readline().rstrip()

def cap(s):
    ans = ''
    for i in s:
        if i.isupper(): # 대문자인지 검사
            ans+=i
    return ans

def check(ans):
    result = ''
    alpha = ['U','C','P','C']
    for i in ans: # U,C,P,C의 순서로 만든다.
        if not alpha: # 다 만들었으면 종료
            break
        if i == alpha[0]:
            result+=i
            alpha.pop(0)
    return result

if check(cap(s)) == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')