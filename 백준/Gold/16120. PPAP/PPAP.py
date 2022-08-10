import sys

s = sys.stdin.readline().strip()

stack = []
ppap = ['P','P','A','P']
if s == 'PPAP' or s == 'P':
    print('PPAP')
else:
    for i in range(len(s)):
        stack.append(s[i])
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()
    if stack == ppap or stack == ['P']:
        print('PPAP')
    else:
        print('NP')