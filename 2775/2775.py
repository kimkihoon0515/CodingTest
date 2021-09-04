t = int(input()) # Test case의 갯수를 받아온다.

for i in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1,n+1)] # 0층에 사는 사람들의 배열
    for j in range(k):
        for x in range(1,n):
            people[x] +=people[x-1]
    print(people[-1])
