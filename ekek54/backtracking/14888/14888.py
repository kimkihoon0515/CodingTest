import sys
N= int(sys.stdin.readline())
nums= list(map(int,sys.stdin.readline().split(' ')))
symbols=['1','2','3','4']
array=list(map(int, sys.stdin.readline().split(' '))) #기호의 개수 배열/ 기호를 하나 사용하면 개수를 감소시켜 기호 사용 현황 체크 가능
result_list=list()
symbol_list=list()
def result():  # 식 계산을 위한 함수
    result = nums[0]
    for i in range(N - 1):
        if symbol_list[i] == 0:
            result += nums[i + 1]
        elif symbol_list[i] == 1:
            result -= nums[i + 1]
        elif symbol_list[i] == 2:
            result *= nums[i + 1]
        elif symbol_list[i] == 3:
            if result < 0:
                result *= -1
                result //= nums[i + 1]
                result *= -1
            else:
                result //= nums[i + 1]
    return result

def dfs(cnt):
    if (cnt == N - 1):
        result_list.append(result())
    for j in range(4):
        if array[j] == 0:
            continue
        array[j] -= 1
        symbol_list.append(j)
        dfs(cnt + 1)
        array[j] += 1
        symbol_list.pop(cnt)  # pop을 쓰는 이유 : remove(symbols[j])하면 제거를 원하는 기호와 동일한 기호중 앞 인덱스의 원소가 제거 되서 순서가 뒤섞임

dfs(0)
print(max(result_list))
print(min(result_list))