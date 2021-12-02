def solution(array, commands):
    #[1,5,2,6,3,7,4] [[2,5,3],[4,4,1],[1,7,3]] [5,6,3]
    answer = []
    for i in range(len(commands)):
        a,b,c = commands[i][0],commands[i][1],commands[i][2]
        arr = []
        for j in range(a-1,b):
            arr.append(array[j])
        arr.sort()
        answer.append(arr[c-1])
    return answer