from collections import deque
def solution(progresses, speeds):
    answer = []
    progress = deque(progresses)
    speed = deque(speeds)
    t = 0
    cnt = 0
    
    while progress:
        if progress[0] + t * speed[0] > 99: # 만약 deque의 첫 번째 일이 종료된다면
            progress.popleft() 
            speed.popleft()
            cnt +=1 # 개수 1개 늘려준다.
        else:
            t +=1 # 아직 종료되지 않았다면 시간을 늘려준다.
            if cnt > 0: # 만약 첫 번째 일이 마감안되었는데
                answer.append(cnt) # 그 뒤에있는 일들이 먼저 마감될 경우 answer에 넣는다.
                cnt = 0 # 다시 제출된 일의 개수를 0으로 만든다.
    answer.append(cnt)
    return answer