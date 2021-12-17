import sys

n = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip().split('*')

left = len(pattern[0])
right = len(pattern[-1])

for _ in range(n):
    s = sys.stdin.readline().strip()
    l = s[:left]
    s = s[left:]
    r = s[len(s)-right :]
    
    if len(s) == 1:
        print('NE')
    elif l == pattern[0] and r == pattern[-1]:
        print('DA')
    else:
        print('NE')