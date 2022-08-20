import sys

g = int(sys.stdin.readline()) # 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 값

# a^2 - b^2 = g

weight = [i*i for i in range(1,g+1)]

end = 0 

ans = []
flag = False
for start in range(g):
    summary = weight[start]
    while end < g:
        summary = weight[end]-summary
        if summary == g:
            flag = True
            print(int(weight[end]**0.5))
            break
        elif summary > g:
            break
        else:
            summary = weight[start]
            end +=1
    
if not flag:
    print(-1)