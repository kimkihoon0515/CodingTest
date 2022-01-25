import sys

n = int(sys.stdin.readline())

score = [list(sys.stdin.readline().split()) for _ in range(n)]

score = sorted(score, key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0])) # 국어는 내림차순, 영어는 오름차순, 수학은 내림차순, 이름은 알파벳 순서
for i in range(n):
    print(score[i][0])
#print(score)