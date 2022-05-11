# 풀이 참고
n = int(input())
inp = []
word = []
for i in range(n):
    inp.append(input())     # 'dog'
    
word = [sorted(list(inp[i])) for i in range(n)] #  [['d','g','o'], ... ]
find = [len(inp[i]) if len(inp[i]) >= len(word[0]) else len(word[0]) for i in range(n)]
# 첫번째 단어보다 긴 경우는 그 길이 만큼, 짧은 경우는 첫번째 단어 길이 만큼 배열 생성

for i in range(1,n):
    for j in range(len(word[0])):      # ['d', 'g', 'o']
        for k in range(len(word[i])):    # ['d', 'g', 'o']
            if word[i][k] == word[0][j]:  # 글자 비교해서 같으면 find -= 1
                find[i] -= 1
                word[i][k] = ' '     # 글자 지움
                break

cnt = 0            
for i in range(1,n):
    if find[i] <= 1:    # 1더하거나, 1빼거나, 1수정, 모든 문자 같은 경우 cnt += 1
        cnt += 1
print(cnt)