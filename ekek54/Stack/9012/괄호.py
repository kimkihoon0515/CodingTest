import sys

def VPS(arr):
    while(1):
        if '()' not in arr:
            if len(arr)==0:
                return 'YES'
            else:
                return 'NO'
        else:
            arr = arr.split('()')
            arr = "".join(arr)


N = int(sys.stdin.readline())
for i in range(N):
    arr = sys.stdin.readline().rstrip('\n')
    print(VPS(arr))