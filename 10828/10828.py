import sys
n = int(sys.stdin.readline()) # 기존에 하던방식으로 input을 사용하면 시간초과가 뜨므로 sys.stdin.readline()활용


li = []
s = []
for i in range(n):
    s = list(map(str,sys.stdin.readline().split()))
    if len(s) == 1:
        if s[0] == 'top':
            if len(li) > 0:
                print(li[len(li)-1])
            else:
                print(-1)
        if s[0] == 'size':
            print(len(li))
        if s[0] == 'pop':
            if len(li) > 0:
                print(li[len(li)-1])
                li.pop()
            else:
                print(-1)
        if s[0] == 'empty':
            if len(li) == 0:
                print(1)
            else:
                print(0)
    else:
        li.append(s[1])
