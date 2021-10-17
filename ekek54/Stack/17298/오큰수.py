import sys
N = int(sys.stdin.readline())
arr= list(map(int,sys.stdin.readline().split(' ')))
res= [0 for i in range(N)]
stack=[]

def top(stack):
    return stack[len(stack)-1]

for i in range(N):
    if i == 0:
        stack.append([i,arr[i]])
    else:
        while(1):
            if top(stack)[1] >= arr[i]:
                stack.append([i,arr[i]])
                break
            else:
                tmp = stack.pop()
                res[tmp[0]] = arr[i]
                if len(stack) == 0:
                    stack.append([i,arr[i]])
                    break
if len(stack) != 0:
    for i in stack:
        res[i[0]]= -1
print(*res)