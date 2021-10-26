n = int(input())
li = [] # 각 회의의 시작시간과 끝나는 시간이 배열에 입력된다.
for i in range(n):
    li.append(list(map(int,input().split())))
li.sort(key=lambda x: x[0]) # 시작시간에 따라 정렬을 한번 해준다.
li.sort(key=lambda x: x[1]) # 끝나는 시간에 따라 정렬을 한번 더 해준다. 

cnt = 0 
finish = 0 # 끝나는 시간을 저장하기 위한 변수 
for i in range(n): # 각 회의가 시작하는 시간이 그 전 회의의 끝나는 시간과 같거나 크면 그 회의의 끝나는 시간을 새로운 finish로 정의한다.
    if li[i][0] >= finish:
        cnt +=1 # 그렇게 진행될 수 있는 회의의 개수를 저장한다.
        finish = li[i][1]
print(cnt)