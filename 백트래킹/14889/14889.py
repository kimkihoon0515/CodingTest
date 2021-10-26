import itertools # combination import해줌
n = int(input()) # n을 입력받음

link = [list(map(int, input().split())) for _ in range(n)] # n x n 행렬의 형태로 숫자를 저장
num = [] # 0~n까지의 숫자를 배열에 저장 
team = [] # 조합의 종류를 저장하는 배열

for i in range(n):
    num.append(i)

min_stat = 100000


for i in list(itertools.combinations(num,n//2)):
    team.append(i)


for i in range(len(team)//2): # 반복문을 돌리는데 총 필요한 갯수는 팀의 조합의 갯수 % 2 
    team_member = team[i] # i번째 팀의 조합을 변수로 지정
    start_stat = 0 # start 팀의 스탯을 선언해준다
    for j in range(n//2): # 팀에는 플레이어가 n//2만큼 들어가있으므로 그것을 반복문을 돌려준다.
        member = team_member[j] # i번째 팀의 조합에서 각각의 플레이어를 지정해주는 변수
        for k in team_member: # 한 개의 팀의 조합만큼 반복문을 돌려서 start 팀의 스탯을 저장한다.
            start_stat += link[member][k]
    
    team_member = team[-i-1] # start 팀을 제외한 나머지 멤버로 구성된 팀을 다시 team member에 저장하고
    link_stat = 0 # link 팀의 스탯을 변수로 선언해준다.
    for j in range(n//2): # start 팀과 마찬가지로 각각의 멤버의 스탯의 합을 구해준다.
        member = team_member[j]
        for k in team_member:
            link_stat += link[member][k]
    
    min_stat = min(min_stat,abs(start_stat-link_stat)) # 스탯의 차의 최소값을 변수로 지정해주고 그것을 출력한다.

print(min_stat)

