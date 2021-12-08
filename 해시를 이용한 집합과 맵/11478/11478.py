import sys
s = sys.stdin.readline().strip()    


result = list(s) # s의 각 문자를 list로 분리
S = ''

for start in range(len(s)): 
    end = start+1 
    S = s[start] # 시작주소부터 S에 넣는다.
    while end < len(s): 
        S+=s[end] # 끝지점까지 S에 추가하고 
        end +=1
        result.append(S) # 결과배열에 넣는다.
    
print(len(set(result))) # 마지막에 원소의 개수를 출력한다.


