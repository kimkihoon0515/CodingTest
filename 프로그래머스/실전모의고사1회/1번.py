from collections import Counter

def solution(X, Y):
    answer = ''

    x = Counter(X)
    y = Counter(Y)

    ans = []

    for key,value in x.items():
        if key in y:
           minimum = min(value,y[key])
           for i in range(minimum):
               ans.append(key)
               
    if not ans:
        return '-1'
    else:
        ans.sort(reverse=True)

        if ans[0] == '0':
            return '0'
        else:
            answer = ''.join(ans)

    return answer