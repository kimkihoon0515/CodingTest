# 내가 푼 풀이
def solution(sizes):
    for i in range(len(sizes)): # 상자의 가로 세로 길이중 긴 것을 무조건 왼쪽으로 몰아놓기
        tmp = 0
        if sizes[i][0] < sizes[i][1]: 
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
    a = sorted(sizes,key=lambda x: -x[0]) # x[0] 의 내림차순으로 정렬
    x = a[0][0] # 가장 큰 값
    b = sorted(sizes,key=lambda x: -x[1]) # x[1] 의 내림차순으로 정렬
    y = b[0][1] # 가장 큰 값
    answer = x * y 
    return answer

# 베스트 풀이
'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    [60,50],[60,30],[30,70],[80,40] 중 각각의 x,y 좌표중 큰 값들 중 최대값 * x,y 좌표중 작은 값들 중 최대값
'''