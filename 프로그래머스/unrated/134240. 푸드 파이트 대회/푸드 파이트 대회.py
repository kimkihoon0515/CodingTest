def solution(food):
    list =[food[i]//2 for i in range(1, len(food))]

    res = ''
    for number, remainder in enumerate(list,start=1):
        if remainder == 0:
            pass
        else:
            res += str(number) * remainder
    return res + '0' + res[::-1]
 