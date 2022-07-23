import sys

n = int(sys.stdin.readline().strip())
crane = list(map(int,sys.stdin.readline().split()))
crane.sort(reverse=True)

m = int(sys.stdin.readline())
box = list(map(int,sys.stdin.readline().split()))
box.sort(reverse=True)
if max(box)>max(crane):
    print(-1)
else:
    cnt = 0
    while box:
        for i in crane:
            for j in box:
                if i>=j:
                    box.remove(j)
                    break
        cnt+=1
    print(cnt)