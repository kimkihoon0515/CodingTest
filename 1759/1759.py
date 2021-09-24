from itertools import combinations 
l,c = map(int,input().split()) # l과 c를 입력받는다.
word = sorted(list(map(str,input().split()))) # 입력받은 알파벳들을 순서대로 정렬해서 배열에 입력한다.
result =[] # 순열 조합의 배열을 만든다.
result.extend(list(map(''.join,combinations(map(str,word),l))))
moum = ['a','e','o','u','i']

for i in result:
    vows = 0 # 모음
    coms = 0 # 자음
    for j in i: # result 배열에 들어가있는 조합들을 차례로 반복문 돌려서 그 속에 자음이 몇개 모음이 몇개 들어있는지 파악한다.
        if j in moum:
            vows +=1
        else:
            coms +=1
    if vows >=1 and coms >=2: # 조건에 맞는 i를 출력한다.
        print(i)