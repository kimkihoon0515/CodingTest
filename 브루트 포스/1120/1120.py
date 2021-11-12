import sys

a,b = list(sys.stdin.readline().split())
result = []
for i in range(len(b)-len(a)+1): # a와 b가 같을 경우에도 동작하기위해 +1을 해줌 안그러면 0~0까지라 돌지 않는다.
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]: # a의 문자열을 b에 한칸씩 증가시키면서 비교한다. 다를때마다 cnt를 하나씩 증가시킨다.
            cnt +=1
    result.append(cnt)

print(min(result)) # 차이가 가장 적은 것을 출력한다.