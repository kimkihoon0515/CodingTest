import sys

n = int(sys.stdin.readline())

def fac(n):
    if n<2:
        return n
    return n*fac(n-1)

result = str(fac(n))

if result == str(0):
    print(0)
else:


    cnt = 0

    for i in reversed(range(len(result))):
        if int(result[i]) != 0:
            break
        else:
            cnt+=1

    print(cnt)