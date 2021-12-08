import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = [list(map(str,sys.stdin.readline().split())) for _ in range(n)] # 옷을 입력받고
    dic = dict() # hash 형태로 각 종류에 따라 분리한다.
    for k,v in clothes:
        dic[v] = dic.get(v,0)+1
    result = [v for k,v in dic.items()] # value 값만 빼서 배열에 저장하고 
    answer = 1
    for i in result: # 결과값을 출력한다.
        answer *=(i+1)
    print(answer-1)