import sys

s = sys.stdin.readline().rstrip()

def cap(s):
    ans = ''
    for i in s:
        if i.isupper():
            ans+=i
    return ans

def check(ans):
    result = ''
    alpha = ['U','C','P','C']
    for i in ans:
        if not alpha:
            break
        if i == alpha[0]:
            result+=i
            alpha.pop(0)
    return result

if check(cap(s)) == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')