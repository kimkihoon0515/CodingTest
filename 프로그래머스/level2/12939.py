def solution(s):
    answer = ''
    li = list(map(int,s.split())) # 공백 기준으로 int형으로 list 선언
    #print(li)
    li.sort() # 정렬
    print(li)
    answer += str(li[0]) # 최소값
    answer += ' ' # 공백더해주기
    answer += str(li[-1]) # 최대값
    return answer