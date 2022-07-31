def solution(dirs):
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    dir = {'U':3,'D':2,'R':0,'L':1}
    visit = set()
    x, y = 0,0
    for i in range(len(dirs)):
        direction = dir[dirs[i]]
        nx = x + dx[direction]
        ny = y + dy[direction]
        if -5<=nx<=5 and -5<=ny<=5:
            if (x,y,nx,ny) not in visit:
                visit.add((x,y,nx,ny))
                visit.add((nx,ny,x,y))
                answer+=1
        else:
            continue
        x,y = nx,ny
    return answer