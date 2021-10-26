n = int(input()) # n을 입력받는다
end_num = 666 # 처음 종말의 숫자는 666
cnt = 0 # n의 값과 비교하기 위한 변수
while True:
    if '666' in str(end_num): # 666이 end_num에 있으면 cnt를 하나씩증가시켜서 cnt와 n이 같아지면 종료 아니면 end_num을 하나씩 증가
       cnt+=1
    if cnt == n:
        print(end_num)
        break 
    end_num+=1