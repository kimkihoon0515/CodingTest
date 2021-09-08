n = int(input()) # 원판의 갯수를 입력받는다.
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

tower = 1

for i in range(n-1):
    tower = 2 * tower +1
print(tower)
hanoi(n,1,2,3)