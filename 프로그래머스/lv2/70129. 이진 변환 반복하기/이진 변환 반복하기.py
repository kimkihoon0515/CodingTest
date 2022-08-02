def solution(s):
    answer = []
    cnt = 0
    idx = 0
    while s!='1':
        new = ''
        for i in range(len(s)):
            if s[i] == '1':
                new+='1'
            else:
                cnt +=1
        s = bin(len(new))[2:]
        idx +=1
    answer= [idx,cnt]
    return answer

