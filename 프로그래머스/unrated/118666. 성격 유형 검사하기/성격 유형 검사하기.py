def solution(survey, choices):
    answer = ''
    # n 1 c 1 m 2 t 3 a 1
    
    result = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i] == 1:
            if survey[i][0] not in result:
                result[survey[i][0]] = 3
            else:
                result[survey[i][0]] +=3
                
        if choices[i] == 2:
            if survey[i][0] not in result:
                result[survey[i][0]] = 2
            else:
                result[survey[i][0]] +=2
                
        if choices[i] == 3:
            if survey[i][0] not in result:
                result[survey[i][0]] = 1
            else:
                result[survey[i][0]] +=1
                
        if choices[i] == 5:
            if survey[i][1] not in result:
                result[survey[i][1]] = 1
            else:
                result[survey[i][1]] +=1
                
        if choices[i] == 6:
            if survey[i][1] not in result:
                result[survey[i][1]] = 2
            else:
                result[survey[i][1]] +=2
                
        if choices[i] == 7:
            if survey[i][1] not in result:
                result[survey[i][1]] = 3
            else:
                result[survey[i][1]] +=3
        else:
            continue
            
    if result['R']>= result['T']:
        answer+='R'
    else:
        answer+='T'
    
    if result['C']>= result['F']:
        answer+='C'
    else:
        answer+='F'
    
    if result['J']>=result['M']:
        answer+='J'
    else:
        answer+='M'
        
    if result['A']>=result['N']:
        answer+='A'
    else:
        answer+='N'
    
    
    return answer