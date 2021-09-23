from itertools import combinations

nums=[] # 입력한 숫자들 중 배열에 저장할 숫자들을 저장해놓을 배열
lotto = [] # 로또번호들을 저장해놓을 배열
while(True):
    n = list(map(int,input().split())) # k와 s를 포함하는 숫자들을 입력받고 0을 입력받으면 반복문을 멈춘다.
    if n[0] == 0:
        break
    else:
        for i in range(len(n)-1): # 입력받은 숫자들 중 1~n까지의 숫자를 배열에 저장하고 그것을 combination화한다.
            nums.append(n[i+1])
    lotto.extend(list(map(' '.join,combinations(map(str,nums),6))))
    for i in range(len(lotto)):
        print(lotto[i]) # i번째 lotto를 출력하고 전부다 출력하면 초기값으로 설정을 되돌린다.
    nums.clear()
    lotto.clear()
    print()
    
