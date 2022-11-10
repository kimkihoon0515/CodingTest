def solution(common):
    for i in range (len(common)):
        if common[i+2] - common[i+1] == common[i+1] - common[i]:
            return common[-1] + (common[i+2] - common[i+1])
        else:
            return common[-1] * (common[i+2] / common[i+1])