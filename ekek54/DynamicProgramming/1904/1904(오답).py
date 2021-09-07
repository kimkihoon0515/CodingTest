def fib(N):
    if len(fib_arr) >= N:
        return fib_arr[N-1]
    fib_arr.append((fib(N-1)+fib(N-2))%15746)
    return fib_arr[N-1]
import sys
N= int(sys.stdin.readline())
fib_arr = [1, 2]
print(fib(N))
#문제의 수열은 피보나치이며 피보나치 결과들을 리스트에 저장하는 방식
#해당 문제는 재귀로 풀면 런타임에러 최대 재귀 제한 발생
#관련 포스트:https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=luiz4our&logNo=220642911892
