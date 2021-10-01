n = int(input()) # 전기줄을 연결할 칸의 개수를 입력받는다.

li = [] # 전기줄의 각각의 연결상태를 저장할 배열을 만들고 입력받는다.
result = [1] * n # 최소 몇 개의 전기줄을 없앨 것인지 그 배열을 저장한다.
for _ in range(n):
    li.append(list(map(int,input().split())))
li.sort() # A로 우선 정렬을 하고 그 다음 B에서는 가장 긴 증가하는 수열을 구하면 된다. 
for i in range(n): 
    for j in range(i):
        if li[i][1] > li[j][1]:
            result[i] = max(result[i],result[j]+1)

print(n-max(result))

