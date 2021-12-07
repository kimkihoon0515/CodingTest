# 내 풀이
def solution(arr1, arr2):
    answer = []
    #print(arr1,arr2)
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            result.append(sum)
        answer.append(result)
    return answer

# 다른 사람 풀이 zip 사용

def solutions(X,Y):
    answer = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer
