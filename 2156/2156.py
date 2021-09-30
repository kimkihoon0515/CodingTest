n = int(input()) # 포도주의 개수를 입력받는다.

li = [0] # 각 포도주 잔의 양을 저장하는 배열을 만든다.

for i in range(n): # 각 포도주 잔의 양을 배열에 저장한다.
    li.append(int(input()))

result = [0] # 합을 계산하는 배열을 만들고 첫 번째와 두 번째 규칙을 저장해놓는다.
result.append(li[1])
result.append(li[1]+li[2])

for i in range(3,n+1): # 3 번째 부터는 새로운 규칙이 생기는데 3가지 경우가 항상 생긴다. 
    result.append(max(result[i-1],result[i-2]+li[i],result[i-3]+li[i]+li[i-1])) # i번째 포도잔을 먹는 경우와 안먹는 경우로 나뉘는데 안먹으면 i-1번째까지의 규칙과 같다 먹으면 또 2가지로 나뉘는데 그것을 정리해서 3가지중 max 값을 배열에 저장한다.
print(result[n])