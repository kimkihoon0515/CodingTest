def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),10:(3,0),0:(3,1),11:(3,2)} # keypad 저장
    left = 10 # 왼손 현재위치
    right = 11 # 오른손 현재위시
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = number
        elif number in [3,6,9]:
            answer += 'R'
            right = number
        elif number in [2,5,8,0]:
            l_distance = abs(keypad[number][0]-keypad[left][0])+abs(keypad[number][1]-keypad[left][1]) # 왼손거리
            r_distance = abs(keypad[number][0]-keypad[right][0])+abs(keypad[number][1]-keypad[right][1]) # 오른손거리
            if l_distance < r_distance: 
                answer += 'L'
                left = number
            elif l_distance == r_distance: # 같으면 왼손잡이인지 오른손잡이인지 검사
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
            else:
                answer += 'R'
                right = number
                    
    return answer