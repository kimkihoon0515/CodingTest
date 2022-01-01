paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    #사각형 부분만 1로 바꾸어줌
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += sum(row)
print(answer)