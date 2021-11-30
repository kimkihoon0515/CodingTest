import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

dice = []

sum = 0

if n == 1: # 주사위 개수가 1개일 때는 작은 숫자 순서대로 5면을 합치면 되므로
    li.sort()
    for i in range(5):
        sum += li[i]
else: # 주사위전개도에서 면을 합치면 나오는 조합중 작은 숫자만 따로 빼서 3개 집어넣는다.
    dice.append(min(li[0],li[5]))
    dice.append(min(li[1],li[4]))
    dice.append(min(li[2],li[3]))
    dice = sorted(dice)
    
    a = (n-2)*(n-2) + 4*(n-2)*(n-1) # 가장 작은 숫자의 면이 보여질 때 주사위 개수
    b = 4*(n-2) + 4*(n-1) # 그 다음 작은 면이 보여질 때 주사위 개수
    c = 4 # 그 다음으로 작은 면이 보여질 때 주사위 개수
    
    min1 = dice[0] # 가장 작은 면
    min2 = dice[0]+dice[1] # 그 다음으로 작은 면
    min3 = dice[0]+dice[1]+dice[2] # 그 다음으로 작은 면
    
    sum += a *min1 + b*min2 + c*min3 # 최소값들의 합
print(sum)    