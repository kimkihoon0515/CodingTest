import sys

n = int(sys.stdin.readline())

score = [list(sys.stdin.readline().split()) for _ in range(n)]

score = sorted(score, key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in range(n):
    print(score[i][0])
#print(score)