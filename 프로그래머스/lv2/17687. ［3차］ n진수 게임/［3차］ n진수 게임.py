notation = '0123456789ABCDEF'
def func(number,base):
    q,r = divmod(number,base)
    n = notation[r]
    return func(q,base) + n if q else n

def solution(n, t, m, p):
    answer = ''
    numbers = []
    for i in range(0,m*t):
        if len(numbers)>m*t:
            break
        else:
            num = func(i,n)
            for j in range(len(num)):
                if len(numbers)>m*t:
                    break
                numbers.append(num[j])
    for i in range(p-1,len(numbers),m):
        answer+=numbers[i]
    answer = answer[:t]
    return answer