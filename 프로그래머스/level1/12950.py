def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): # 열의 길이
        sum = []
        for j in range(len(arr1[0])): # 행의 길이
            sum.append(arr1[i][j]+arr2[i][j]) # 행렬 A + B를 열의 개수만큼 반복해서 sum 배열에 넣고 answer에 넣는다.
        answer.append(sum)
    return answer