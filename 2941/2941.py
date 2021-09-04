a = input() # str 형태로 입력받는다.
croa_list = ["c=","c-","dz=","d-","lj","nj","s=","z="] # 크로아티아 알파벳으로 이루어진 배열을 선언한다.
cnt = 0 # 크로아티아 배열의 개수를 저장할 변수를 선언한다.
for i in croa_list: # 배열에서 반복문을 돌려서 크로아티아 문자를 찾는다.
    index = a.count(i) # index로 a에서 크로아티아 알파벳을 찾는다. ex:) 2 0 0 0 0 0 0 0 이런식으로 출력
    cnt+=index # cnt에 index를 계속 반복해서 더해준다.
count = len(a) - cnt*2 # 크로아티아 알파벳은 개수가 2이므로 cnt에 2를 곱한 값을 a의 길이에서빼준다. -> 크로아티아 알파벳이 아닌 문자를 찾는 식
print(count+cnt)  
