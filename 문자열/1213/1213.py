import sys
from collections import Counter

s = sys.stdin.readline().strip()

word = Counter(s)

def even(s): # 총 문자열 길이가 짝수개일 경우
    ans = ''
    for k,v in sorted(word.items()): # 사전순으로 출력해야하므로
        if v %2 !=0: # 알파벳 개수가 홀수개가 나오면안되므로
            return False
        ans += k * int(v//2) # 반반 나눠서 하나는 제대로 하나는 거꾸로 출력
    return ans+ans[::-1]

def odd(s): # 문자열 길이가 홀수개일 경우
    cnt = 0
    ans = ''
    for k,v in sorted(word.items()):
        if v % 2 !=0: # 홀수개의 알파벳이 있는경우
            cnt +=1 
            mid = k # 그 알파벳을 중앙에 둬야하므로
            if cnt >1:
                return False # 만약 홀수개의 알파벳이 2개이상인 경우에 회문 못만드므로
        ans += k * int(v//2) # 반반나눠서 하나는 제대로 중간에 홀수개의 알파벳을 넣고 그 다음에는 거꾸로 출력
    
    return ans + mid + ans[::-1]

if len(s) % 2 == 0:
    if not even(s):
        print("I'm Sorry Hansoo")
    else:
        print(even(s))
else:
    if not odd(s):
        print("I'm Sorry Hansoo")
    else:
        print(odd(s))