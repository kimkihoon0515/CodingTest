import sys

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break

    num = 0
    i = 1
    while True:
        num = num*10 + 1
        num%=n
        if num == 0:
            print(i)
            break
        i +=1