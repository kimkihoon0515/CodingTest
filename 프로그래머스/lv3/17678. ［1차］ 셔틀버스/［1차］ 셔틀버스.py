def solution(n, t, m, timetable):
    answer = 0
    crewtime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewtime.sort()
    bus = [9*60 + t*i for i in range(n)]
    
    i = 0
    for j in bus:
        cnt = 0
        while cnt <m and i < len(crewtime) and crewtime[i]<=j:
            i+=1
            cnt+=1
        if cnt < m :
            answer = j
        else:
            answer = crewtime[i-1]-1
    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)