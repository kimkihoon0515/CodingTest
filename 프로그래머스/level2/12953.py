import math
def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = (answer * i) // math.gcd(answer,i) # 최대 공약수를 구하고 최소공배수는 그것을 반복문 돌리면서 구할 수 있다.
    return answer