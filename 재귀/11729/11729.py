n = int(input()) # 원판의 갯수를 입력받는다.
def hanoi(n,a,b,c): # 하노이 탑 알고리즘 n은 탑의 갯수 a는 출발지 b는 거쳐가는 곳 c는 도착지점
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

tower = 1 # 하노이 탑의 이동 개수를 받기 위한 변수

for i in range(n-1): # 하노이 탑은 a(n) = a(n-1) * 2 + 1 의 규칙으로 이동한 갯수가 정해진다.
    tower = 2 * tower +1

print(tower)
hanoi(n,1,2,3)