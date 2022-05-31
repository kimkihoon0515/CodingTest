import math


def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1:  # i == 1인 경우는 문제에서는 0으로 주어짐
            answer.append(0)
        else:
            # 소수인지 아닌지 판별하기 위해
            # 판별하기 위한 숫자 i 의 제곱근 까지 하나씩 나눠보고
            # 소수가 아니면 몫을, 소수이면 1을 넣는다.
            sqrt = int(math.sqrt(i))
            for j in range(2, sqrt + 1):
                mok = i // j
                # !!!!중요!!!! - 정확성에서는 통과하나 효율성에서 통과하지 못하는 이유가 있음
                # 전체 길이는 10**9이지만 블록은 10**7 이다
                # 그러므로 몫이 10**7을 넘어가면 안됨!!
                if mok > 10 ** 7:
                    continue
                if i % j == 0:
                    answer.append(mok)
                    break
            else:
                answer.append(1)

    return answer