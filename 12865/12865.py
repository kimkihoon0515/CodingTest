n,k = map(int,input().split()) # n 개의 물건이 있고 각 물건은 무게 W와 가치 V를 가진다. 최대 K 무게만큼의 무게만을 넣은 배낭을 갖고다닐 수 있다.

result = [[0] *(k+1) for i in range(n+1)] # 무게의 합의 최대값을 저장할 배열

for i in range(1,n+1): # 현재 가방의 허용 무게보다 넣을 물건이 크면 안넣는다.
    w,v = map(int,input().split())
    for j in range(1,k+1):
        if j <w:
            result[i][j] = result[i-1][j]
        else: # 그렇지않으면 현재 넣을 물건의 무게만큼 배낭에서 빼고 현재물건을 넣는것과 이전 배낭 그대로 가지고 가는 것 중 최대값을 고른다.
            result[i][j] = max(result[i-1][j],result[i-1][j-w]+v)
print(result[n][k]) # 배열의 가장 마지막 값이 최대값이므로 그것을 출력한다.