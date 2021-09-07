t = int(input()) # Test case의 갯수를 받아온다.

for i in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1,n+1)] # 0층에 사는 사람들의 배열
    for j in range(k): # 층 수 만큼 반복문을 돌린다.
        for x in range(1,n): # 사람 수 -1 까지 반복문 돌린다.
            people[x] +=people[x-1] # 거주자의 수를 변경한다.
    print(people[-1]) # 마지막 거주자를 불러온다.
