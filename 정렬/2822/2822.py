import sys

score = list(int(sys.stdin.readline().strip()) for _ in range(8))

ans = []
for (index,values) in enumerate(score):
    ans.append((index+1,values))

ans = sorted(ans,key=lambda x:x[1],reverse=True) # 점수가 높은 역순으로 정렬
ans.pop(-1) # 제일 낮은 점수 3개 없애기
ans.pop(-1)
ans.pop(-1)

result = []

sum = 0
for (index,values) in ans: # index는 result에 점수는 sum에 넣는다.
    result.append(index)
    sum += values

result = sorted(result)

print(sum)
print(*result)

    