from itertools import combinations

def check(relation,x): # unique를 만족하는제 체크하는 함수

    li = []
    for i in range(row):
        tmp = []
        for j in range(len(x)):
            tmp.append(relation[i][x[j]])
        if tmp in li:
            return False
        li.append(tmp)
    return True

def solution(relation):
    answer = 0
    global row
    row = len(relation) # 가로 한 줄
    column = len(relation[0]) # 가로 중 한 칸
    
    result = []
    for i in range(1,column+1):
        result.append(list(combinations(range(column),i))) # 뽑을 수 있는 모든 조합
    
    uni = []
    for i in range(len(result)): 
        for j in range(len(result[i])):
            if(check(relation,result[i][j])): # 유일성을 만족하면 uni 에 넣는다.
                uni.append(result[i][j])
    
    li = set(uni) # set을 통해 최소성을 파악한다.
    for i in range(len(uni)):
        for j in range(i+1,len(uni)):
            if len(uni[i]) == len(set(uni[i]) & set(uni[j])): # 겹치는 원소가 있으면
                li.discard(uni[j]) # li에서 제외한다.
    answer = len(li)
    return answer