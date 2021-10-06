import sys

N = int(sys.stdin.readline())
seq = [int(sys.stdin.readline()) for i in range(N)]
stack = [0]
res=[]
i=1
j=0
while(1):
    if j == N:
        for k in res:
            print(k)
        break
    if stack[len(stack)-1] < seq[j]:
        stack.append(i)
        i += 1
        res.append('+')
    elif stack[len(stack)-1] == seq[j]:
        stack.pop()
        res.append('-')
        j+=1
    else:
        print("NO")
        break