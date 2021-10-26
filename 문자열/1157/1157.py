a = input().upper() # 입력받은 것을 대문자로 바꿔줌
a_list = list(set(a)) # 중복된 문자 제거해주는 것
cnt = [] # 알파벳 갯수를 세어서 저장하려는 배열

for i in a_list: # 중복된 문자를 제거한 list를 반복문으로 돌려서 확인한다.
    count = a.count(i) # 입력받은 배열에서 대문자로 바꿔준 것들의 갯수를 파악한다.
    cnt.append(count) # cnt라는 배열에 위에서 계산한 값을 넣는다.
if cnt.count(max(cnt))>1: # cnt의 최대값이 2개이상일 경우에는 
    print("?") # ?를 출력하고
else: # 최대값이 1개만나오는 경우에는
    print(a_list[(cnt.index(max(cnt)))].upper()) # 가장 최대로 많이 나온 알파벳을 출력한다.