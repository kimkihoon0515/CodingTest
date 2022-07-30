import sys

n = int(sys.stdin.readline())

answer = ''

def second(n):
    global answer
    a,b = divmod(n,2)
    if a == 0:
        answer+=str(b)
        return 
    else:
        answer += str(b)
        second(a)
        
second(n)
print(answer[::-1])

