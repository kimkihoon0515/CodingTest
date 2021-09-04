a = int(input()) # 몇 개의 문자열을 입력받을 것인지 정하는 변수
ans = 0 
for i in range(a): # a개 만큼 입력을 받는다.
    word = list(map(str,input())) # 문자열을 입력받음
    for j in range(len(word)): # 입력받은 문자열의 길이만큼 반복문을 돌린다.
        if j !=len(word)-1: # 
            if word[j] == word[j+1]: # 중복되는 문자가 있으면 계속진행하고
                pass
            elif word[j] in word[j+1:]: # 중복되는 문자가 없으면 그 글자 다음부터 계속 검사함
                break
        else:
            ans+=1
print(ans)