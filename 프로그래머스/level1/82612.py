def solution(price, money, count):
    # price원, N번 이용하면 가격의 N배, 놀이기구 count번 탄다
    answer = -1
    sum = 0
    for i in range(1,count+1):
        sum += i * price
    if sum <= money:
        answer = 0
    else:
        answer = sum - money
    return answer