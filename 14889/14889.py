import itertools 
n = int(input())

link = [list(map(int, input().split())) for _ in range(n)]
num = []
team = []

for i in range(n):
    num.append(i+1)

min_stat = 100000


team.append(list(itertools.combinations(num,n//2)))


for i in range(n//2):
    team_member = team[i]
    print(team_member)
    start_stat = 0
    for j in range(n//2):
        member = team_member[j]
        print(member)
        for k in team_member:
            start_stat += link[member][k]
    
    team_member = team[-i-1]
    link_stat = 0
    for j in range(n//2):
        member = team_member[j]
        for k in team_member:
            link_stat += link[member][k]
    
    min_stat = min(min_stat,abs(start_stat-link_stat))
    print(min_stat)

