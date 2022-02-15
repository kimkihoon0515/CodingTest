import sys
from collections import Counter

s = sys.stdin.readline().strip()

dic = dict(Counter(s))

def dfs(word,ans):
    
    if ans == len(s): # 만든 문자열의 길이가 같아지면 1을 return 해서 answer에 더해준다.
        return 1
    
    answer = 0
    for key in dic.keys(): # 알파벳 하나씩 뽑는다.
        if word == key: # 뽑은 알파벳과 문자열 맨 마지막 알파벳이 같으면 continue
            continue
        if dic[key] == 0: # 알파벳의 남은 개수가 0이어도 continue
            continue
        dic[key] -= 1 # 나머지 모든 경우에 대해 알파벳의 개수를 1개 줄이고
        answer += dfs(key,ans+1) # 만들어진 문자열의 개수에 +1을 해준다.
        dic[key] += 1 # 알파벳 개수를 돌려놓는다.
    return answer

result = dfs('',0)
print(result)