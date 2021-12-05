def solution(name):
    answer = 0
    alpha = []
    for i in name:
        alpha.append(min(ord(i)-65,ord('Z')-ord(i)+1)) # 알파벳 순서대로 A로부터의 거리중 최소값을 저장한다.
    i = 0
    # 조이스틱을 움직여 글자 완성하기
    while True:
        answer += alpha[i] 
        alpha[i] = 0 # 이동이 끝났으면 값을 0으로 만듬

        # 모든 값이 0이 되면 글자가 완성되었으므로 답을 리턴해줌
        if sum(alpha) == 0:
            return answer

        left, right = 1, 1 # 왼쪽과 오른쪽으로 움직일 거리
        # 이동해야 할 글자가 나올 때까지 반복
        while alpha[i - left] == 0: 
            left += 1
        while alpha[i + right] == 0:
            right += 1

        # left, right 중 최소거리 구하여 다음 위치로 이동
        if right > left:
            answer += left
            i -= left
        else:
            answer += right
            i += right