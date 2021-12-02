def solution(nums):
    answer = 0
    x = len(nums) // 2
    p = []
    for i in nums:
        if i not in p:
            p.append(i)
    if len(p) >= x:
        answer = x
    else:
        answer = len(p)
    return answer