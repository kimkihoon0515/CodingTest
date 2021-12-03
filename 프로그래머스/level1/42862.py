def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost) # 여벌의 옷이 있는 학생이 도난당했을 수 있으므로 더 이상 못빌려주므로 제외.
    set_lost = set(lost) - set(reserve) # 여벌의 옷이 있는 학생이 도난당했을 때 여벌이 있으므로 제외.
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer = n - len(set_lost)
    return answer